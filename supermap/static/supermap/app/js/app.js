//Map init
var
  normalMap = L.supermap.tiandituTileLayer({
    key: "b58c80407f12bc014d44f8b0883e18cc",
    layerType: 'vec',
    attribution: false
  }),

  labelMap = L.supermap.tiandituTileLayer({
    isLabel: true,
    key: "b58c80407f12bc014d44f8b0883e18cc",
    attribution: false
  }),

  terMap = L.supermap.tiandituTileLayer({
    key: "b58c80407f12bc014d44f8b0883e18cc",
    layerType: 'ter',
    attribution: false
  }),

  imgMap = L.supermap.tiandituTileLayer({
    key: "b58c80407f12bc014d44f8b0883e18cc",
    layerType: 'img',
    attribution: false
  }),

  map = L.map('map', {
    center: { lat: 39.914935, lon: 116.407143 },
    maxZoom: 18,
    zoom: 10,
    zoomControl: true,
    layers: [normalMap, labelMap],
    crs: L.CRS.TianDiTu_WGS84,
    logoControl: false,
    attributionControl: false,
  }),

  baseMaps = {
    "标准图": normalMap,
    '地形图': terMap,
    '影像图': imgMap,
  },

  overlayMaps = {
    'Labels': labelMap,
  };

layerContoller = L.control.layers(baseMaps, overlayMaps);
map.addControl(layerContoller);

//添加画图工具
function graph_tool(){
  var options = {
    position: 'topleft',
    drawMarker: true,
    drawPolygon: true,
    drawPolyline: true,
    editPolygon: true,
    deleteLayer: true,
  };
  map.pm.addControls(options);
  //创建画图区域完成事件
  map.on('pm:create', e => {
    let ginfo,
      overlays = {};
    BC_name = prompt("输入商圈名字");
    if(e){
      if(e.layer._latlngs != undefined){
        if(e.layer._latlngs.length == 1){
          overlays[BC_name] = e.layer._latlngs[0];}
        else {overlays[BC_name] = e.layer._latlngs;}
      }
      else if(e != undefined){
        overlays[BC_name] = {"latlng":e.layer._latlng, "radius":e.layer._radius};
      }
      else { alert('图形保存错误，请联系地图管理员'); }
    } else {
      alert('画图错误，请联系地图管理员');
    }
    overlays = JSON.stringify(overlays);
    //异步传输
    $.ajax({
        type: 'GET',
        url: "{% url 'post_coordinate' %}",
        data: {'overlays':overlays},
        dataType: "json",
        contentType:"json/application",
        success: function (response) {},
    });
  });
}

//比例尺控件
L.control.scale().addTo(map);

//版权控件
var prefix = "<a href='https://sz.ke.com/' title='Powerful BI for Business Strategy'>bkMap</a>",
  attribution = "bkMap SZ <span>© <a href='https://sz.ke.com/' target='_blank'>深圳业务策略中心</a></span> with <span>© <a href='https://sz.ke.com/' target='_blank'>数据运营部</a></span>";
L.control.attribution({
  position: 'bottomright',
  prefix: prefix
}).addAttribution(attribution).addTo(map);

graph_tool()
standardMap()