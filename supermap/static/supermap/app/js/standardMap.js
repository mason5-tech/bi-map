function standardMap() {
    // 移除之前图层
    map.removeControl(layerContoller)

    //读取后端数据
    var positions = JSON.parse("{{dict_BC|escapejs}}");
    var shop_info = JSON.parse("{{dict_shop|escapejs}}");

    //画图
    var BJ = L.marker([39.830660058696104, 116.92866163503169]).bindPopup('hello'),
        CD = L.marker([30.40, 104.04]).bindPopup('hello');
    var cities = L.layerGroup([BJ, CD]);

    var polygon1 = L.polygon([
        [39.924232,116.342753],
        [39.940166,116.46291],
        [39.851596,116.395645]
    ]), polygon2 = L.polygon([
        [39.892795,116.515227],
        [39.765129,116.396795],
        [39.743384,116.676204]
    ], {color:'red',fillColor:'blue'});
    var circles = L.layerGroup([polygon1, polygon2]);

    map.addLayer(cities)
    map.addLayer(circles)

    overlayMaps = {
        'Labels': labelMap,
        'Cities': cities,
        'Circles':circles
    };

    layerContoller = L.control.layers(baseMaps, overlayMaps);
    map.addControl(layerContoller);
    
}




