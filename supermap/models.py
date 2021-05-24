from django.db import models


# Create your models here.
class BusinessCircle(models.Model):
    BCname = models.CharField(max_length=50, unique=True)
    count_shops = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.BCname

class ShiyeDaqu(models.Model):
    daqu_name = models.CharField(max_length=50, unique=True)
    count_shops = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.daqu_name

class LianjiaDaqu(models.Model):
    daqu_name = models.CharField(max_length=50, unique=True)
    count_shops = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.daqu_name


class Coordinate(models.Model):
    coordinateFkey = models.ForeignKey(BusinessCircle, on_delete=models.CASCADE, null=True, blank=True)
    coordinate_circle = models.CharField(max_length=50, null=True, blank=True)
    coordinate_x = models.FloatField(default=0, null=True, blank=True)
    coordinate_y = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.coordinate_circle

class ShiyeDaqu_Coordinate(models.Model):
    coordinateFkey = models.ForeignKey(ShiyeDaqu, on_delete=models.CASCADE, null=True, blank=True)
    coordinate_shiyedaqu = models.CharField(max_length=50, null=True, blank=True)
    coordinate_x = models.FloatField(default=0, null=True, blank=True)
    coordinate_y = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.coordinate_shiyedaqu

class LianjiaDaqu_Coordinate(models.Model):
    coordinateFkey = models.ForeignKey(LianjiaDaqu, on_delete=models.CASCADE, null=True, blank=True)
    coordinate_lianjiadaqu = models.CharField(max_length=50, null=True, blank=True)
    coordinate_x = models.FloatField(default=0, null=True, blank=True)
    coordinate_y = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.coordinate_lianjiadaqu

class Shop(models.Model):
    shopFkey = models.ForeignKey(BusinessCircle, on_delete=models.CASCADE, null=True, blank=True)
    shop_code = models.CharField(max_length=20, null=True, blank=True)
    shop_name = models.CharField(max_length=20, null=True, blank=True)
    brand_type = models.CharField(max_length=10, null=True, blank=True)
    shiye_dabu = models.CharField(max_length=10, null=True, blank=True)
    shiye_daqu = models.CharField(max_length=10, null=True, blank=True)
    bk_dabu = models.CharField(max_length=10, null=True, blank=True)
    bk_daqu = models.CharField(max_length=10, null=True, blank=True)
    lianjia_dabu = models.CharField(max_length=10, null=True, blank=True)
    lianjia_daqu = models.CharField(max_length=10, null=True, blank=True)
    dabu = models.CharField(max_length=10, null=True, blank=True)
    daqu = models.CharField(max_length=10, null=True, blank=True)
    draw_bk_daqu = models.CharField(max_length=10, null=True, blank=True)
    draw_lianjia_daqu = models.CharField(max_length=10, null=True, blank=True)
    AECA_code = models.CharField(max_length=20, null=True, blank=True)
    AECA = models.CharField(max_length=10, null=True, blank=True)
    AECAzongjian_code = models.CharField(max_length=20, null=True, blank=True)
    AECAzongjian = models.CharField(max_length=10, null=True, blank=True)
    circle = models.CharField(max_length=10, null=True, blank=True)
    is_circle = models.CharField(max_length=10, null=True, blank=True)
    guishu_area = models.CharField(max_length=10, null=True, blank=True)
    jieyue_date = models.CharField(max_length=10, null=True, blank=True)
    coordinate_x = models.FloatField(default=0, null=True, blank=True)
    coordinate_y = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.shop_name


class ResBlock(models.Model):
    blockFkey = models.ForeignKey(BusinessCircle, on_delete=models.CASCADE, null=True, blank=True)
    resblock_id = models.CharField(max_length=20, null=True, blank=True)
    resblock_name = models.CharField(max_length=50, null=True, blank=True)
    district_name = models.CharField(max_length=10, null=True, blank=True)
    bizcircle_name = models.CharField(max_length=10, null=True, blank=True)
    building_longitude = models.FloatField(default=0, null=True, blank=True)
    building_latitude = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.resblock_name


class ResBlock_ST(models.Model):
    block_STFkey = models.ForeignKey(ResBlock, on_delete=models.CASCADE, null=True, blank=True)
    sign_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    resblock_id = models.CharField(max_length=20, null=True, blank=True)
    resblock_name = models.CharField(max_length=50, null=True, blank=True)
    biz_type = models.CharField(max_length=10, null=True, blank=True)
    subbiz_type = models.CharField(max_length=20, null=True, blank=True)
    agreement_id = models.CharField(max_length=20, null=True, blank=True)
    gmv = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.agreement_id
