from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncMonth, TruncYear

from .models import *


# def pointinpoly_update():
#     def pointinpoly(x, y, list_X, list_Y):
#         yn = False
#         for i in range(0, len(list_X)):
#             if ((list_Y[i] < y and list_Y[i - 1] >= y) or (list_Y[i - 1] < y and list_Y[i] >= y)) and (
#                     list_X[i] <= x or list_X[i - 1] <= x):
#                 yn = (list_X[i] + (y - list_Y[i]) / (list_Y[i - 1] - list_Y[i]) * (list_X[i - 1] - list_X[i]) < x)
#         return yn
#
#     Fkeys = list(map(lambda x: list(x.values())[0], Coordinate.objects.values('coordinateFkey_id').distinct()))
#
#     if Shop.objects.filter(shopFkey_id=None):
#         null_list = Shop.objects.filter(shopFkey_id=None)
#         for i in null_list:
#             id = i.id
#             x = i.coordinate_x
#             y = i.coordinate_y
#             for j in Fkeys:
#                 objects_j = Coordinate.objects.filter(coordinateFkey_id=j)
#                 list_X = list(map(lambda x: x.coordinate_x, objects_j))
#                 list_Y = list(map(lambda x: x.coordinate_y, objects_j))
#                 if pointinpoly(x, y, list_X, list_Y):
#                     Shop.objects.update_or_create(id=id, defaults={'shopFkey_id': j})
#
#
# pointinpoly_update()


def indexView(request):
    geoData_shangquan = json.dumps({'type': "FeatureCollection",
                                    'features': list(map(lambda x: {'type': "Feature", 'properties': {'商圈': x.BCname},
                                                                    'geometry': {'type': "Polygon",
                                                                                 'coordinates': [list(map(
                                                                                     lambda z: [z.coordinate_x,
                                                                                                z.coordinate_y],
                                                                                     x.coordinate_set.all()))]},
                                                                    'count_shops': x.count_shops},
                                                         BusinessCircle.objects.all()))})

    geoData_shiyedaqu = json.dumps({'type': "FeatureCollection",
                                    'features': list(
                                        map(lambda x: {'type': "Feature", 'properties': {'大区': x.daqu_name},
                                                       'geometry': {'type': "Polygon",
                                                                    'coordinates': [list(map(
                                                                        lambda z: [z.coordinate_x, z.coordinate_y],
                                                                        x.shiyedaqu_coordinate_set.all()))]},
                                                       'count_shops': x.count_shops},
                                            ShiyeDaqu.objects.all()))})

    geoData_lianjiadaqu = json.dumps({'type': "FeatureCollection",
                                      'features': list(
                                          map(lambda x: {'type': "Feature", 'properties': {'lj大区': x.daqu_name},
                                                         'geometry': {'type': "Polygon",
                                                                      'coordinates': [list(map(
                                                                          lambda z: [z.coordinate_x, z.coordinate_y],
                                                                          x.lianjiadaqu_coordinate_set.all()))]},
                                                         'count_shops': x.count_shops},
                                              LianjiaDaqu.objects.all()))})

    geoData_loupan = json.dumps({'type': "FeatureCollection",
                                 'features': list(
                                     map(lambda x: {'type': "Feature", 'properties': {'楼盘名称': x.resblock_name},
                                                    'geometry': {'type': "Point",
                                                                 'coordinates': [x.building_longitude,
                                                                                 x.building_latitude]},
                                                    'id': x.resblock_id},
                                         ResBlock.objects.all()))})

    geoData_shop = json.dumps({'type': "FeatureCollection",
                               'features': list(map(lambda x: {'type': "Feature",
                                                               'properties': {'门店名称': x.shop_name, 'AECA': x.AECA,
                                                                              'AECAzongjian': x.AECAzongjian,
                                                                              'bk_daqu': x.bk_daqu,
                                                                              'circle': x.circle,
                                                                              'dabu': x.dabu,
                                                                              'guishu_area': x.guishu_area,
                                                                              'bk_dabu': x.bk_dabu,
                                                                              'brand_type': x.brand_type,
                                                                              'daqu': x.daqu,
                                                                              'lianjia_dabu': x.lianjia_dabu,
                                                                              'lianjia_daqu': x.lianjia_daqu,
                                                                              'shiye_dabu': x.shiye_dabu,
                                                                              'shiye_daqu': x.shiye_daqu},
                                                               'geometry': {'type': "Point",
                                                                            'coordinates': [x.coordinate_x,
                                                                                            x.coordinate_y]},
                                                               'id': x.shop_code
                                                               },
                                                    Shop.objects.all()))})

    return render(request, 'supermap/index.html',
                  {'geoData_shangquan': geoData_shangquan, 'geoData_shiyedaqu': geoData_shiyedaqu,
                   'geoData_lianjiadaqu': geoData_lianjiadaqu, 'geoData_loupan': geoData_loupan,
                   'geoData_shop': geoData_shop})


@csrf_protect
def post_coordinate(request):
    if request.is_ajax and request.method == "POST":
        overlays = json.loads(request.POST.get('overlays'))

        if len(overlays.keys()) > 0:
            key = list(overlays.keys())[0]
            obj, created = LianjiaDaqu.objects.get_or_create(daqu_name=key,
                                                             defaults={'count_shops': 0})
            for j in overlays[key]:
                obj.lianjiadaqu_coordinate_set.get_or_create(coordinate_x=j['lng'], coordinate_y=j['lat'],
                                                             defaults={'coordinate_lianjiadaqu': key})

    return render(request, 'supermap/index.html', None)


def getLoupan(request):
    if request.is_ajax and request.method == "GET":
        graphic_getId = request.GET.get("geoJsonPoint_id", None)
        get_data = ResBlock.objects.get(resblock_id=graphic_getId).resblock_st_set
        if graphic_getId != '' and get_data.all():
            loupanData = get_data.annotate(
                month=TruncMonth('sign_date')).values('month', 'biz_type').order_by('month', 'biz_type').annotate(
                sum_gmv=Sum('gmv'))
            return JsonResponse({"loupanData": list(loupanData)}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)
    else:
        return JsonResponse({}, status=400)


@csrf_protect
def shopInfo_daqu(request):
    if request.is_ajax and request.method == "POST":
        post_data = json.loads(request.POST.get('post_data'))
        type = json.loads(request.POST.get('type'))
        for i in post_data:
            try:
                shop = Shop.objects.get(shop_code=i['id'])
                setattr(shop,type['type'],i['properties'].get('大区'))
            except:
                continue
            finally:
                shop.save()
        return JsonResponse({"valid": True}, status=200)
    else:
        return JsonResponse({}, status=400)
