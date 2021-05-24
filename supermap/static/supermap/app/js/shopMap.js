function echart_pointClassify() {
        var COLORS = ['#e0dffb', '#8c88ef', '#5954e8', '#221cd2', '#17138d', '#0c0a48', '#030314', 'red'];
        var option = {
            tooltip: {},
            visualMap: {
                type: 'piecewise',
                inverse: true,
                top: 110,
                left: 10,
                pieces: [{
                    gt: 0, lte: 2, color: COLORS[0]
                }, {
                    gt: 2, lte: 4, color: COLORS[1]
                }, {
                    gt: 4, lte: 6, color: COLORS[2]
                }, {
                    gt: 6, lte: 8, color: COLORS[3]
                }, {
                    gt: 8, lte: 10, color: COLORS[4]
                }, {
                    gt: 10, lte: 15, color: COLORS[5]
                }, {
                    gt: 15, lte: 20, color: COLORS[8]
                }, {
                    gt: 20, lte: 28, color: COLORS[9]
                }],
                borderColor: '#ccc',
                borderWidth: 2,
                backgroundColor: '#eee',
                dimension: 2,
                inRange: {
                    color: COLORS,
                    opacity: 0.7
                }
            },
            series: [{
                type: 'custom',
                coordinateSystem: "leaflet",
                data: [[116.48454289177835, 39.97630786453111, 5.21, 116.48903446819895, 39.97974971856209],
                [115.97699475625082, 39.683117047909164, 1.38, 115.98148633267142, 39.68657362355323],
                [116.48903446819895, 39.78673903156059, 5.49, 116.49352604461956, 39.79019041448839]],
                renderItem: renderItem,
                animation: false,
                itemStyle: {
                    emphasis: {
                        color: 'pink'
                    }
                },
                encode: {
                    tooltip: 2
                }
            }]
        };
        // 自定义渲染
        function renderItem(params, api) {
            pointLeftTop = map.latLngToContainerPoint(new L.LatLng(api.value(1), api.value(0)));
            pointRightBottom = map.latLngToContainerPoint(new L.LatLng(api.value(4), api.value(3)));

            return {
                type: 'rect',
                shape: {
                    x: pointLeftTop.x,
                    y: pointLeftTop.y,
                    width: pointLeftTop.x - pointRightBottom.x,
                    height: pointLeftTop.y - pointRightBottom.y
                },
                style: api.style({
                    stroke: 'rgba(0,0,0,0.1)'
                }),
                styleEmphasis: api.styleEmphasis()
            };
        }
        function coordsTo4326(coords) {
            var lngLat = L.CRS.EPSG3857.unproject(L.point(coords));
            return [lngLat.lng, lngLat.lat];
        }
        L.supermap.echartsLayer(option).addTo(map);
}