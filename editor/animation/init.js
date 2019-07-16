//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function powerPlantsCanvas(dom, data) {
            if (! data || ! data.ext) {
                return
            }

            $(dom.parentNode).find(".answer").remove()

            const result = data.ext.result
            const output = data.out
            const exp = data.ext.explanation.join('')
            const rows = data.ext.explanation.length
            const cols = data.ext.explanation[0].length
            const result_addon_01 = data.ext.result_addon[1]

            const DELAY = 600
            const RADIUS = 15
            const INTERVAL = 63
            const OFFSET = 25
            const BLUE = '#65A1CF'
            const BASE = '#294270'
            const ORANGE = '#FAAB00'
            const WHITE = '#FFFFFF'

            /*----------------------------------------------*
             *
             * attr
             *
             *----------------------------------------------*/
            const attr = {
                city: {
                    normal: {
                        'stroke': BASE,
                        'stroke-width': 1.5,
                        'fill': WHITE,
                    },
                    powered: {
                        'stroke': BASE,
                        'stroke-width': 1.5,
                        'fill': '#faba00',
                    },
                    plant: {
                        'stroke': BASE,
                        'stroke-width': 2,
                        'fill': '#F0801A',
                        'fill': ORANGE,
                    },
                },
                text: {
                    city: {
                        'stroke': BASE,
                        'font-size': 14,
                    },
                    power: {
                        'stroke': BASE,
                        'stroke-width': 0,
                        'font-size': 9,
                        'fill': WHITE,
                        'fill': BASE,
                    },
                },
                line: {
                    normal: {
                        'stroke-width': 3,
                        'stroke': BLUE,
                    },
                    power: {
                        'stroke-width': 3,
                        'stroke': ORANGE,
                    },
                },
            }

            /*----------------------------------------------*
             *
             * paper
             *
             *----------------------------------------------*/
            const width = INTERVAL*(cols-1)+OFFSET*2
            const height = INTERVAL*(rows-1)+OFFSET*2
            const paper = Raphael(dom, width, height, 0, 0);

            /*----------------------------------------------*
             *
             * input
             *
             *----------------------------------------------*/
            const [network, powers] = data.in
            const power_plants = {}
            output.forEach(([city, power], i)=>{
                power_plants[city] = power
            })

            /*----------------------------------------------*
             *
             * make cities dictionary
             *
             *----------------------------------------------*/
            const cities = {}

            for (let i = 0; i < network.length; i += 1) {
                for (let j = 0; j < 2; j += 1) {
                    const [n1, n2] = [network[i][j], network[i][1-j]]
                    if (! cities[n1]) {
                        cities[n1] = {
                            power: power_plants[n1] || 0,
                            net: [],
                            coord: [
                                exp.indexOf(n1) % cols * INTERVAL + OFFSET,
                                Math.floor(exp.indexOf(n1) / cols) * INTERVAL + OFFSET],
                        }
                    }
                    cities[n1].net.push(n2)
                }
            }

            /*----------------------------------------------*
             *
             * draw power lines
             *
             *----------------------------------------------*/
            const line_dict = {}

            for (let n of network) {
                for (let i = 0; i < 2; i += 1) {
                    const [a, b] = [n[i], n[1-i]]
                    const [x1, y1] = cities[a].coord
                    const [x2, y2] = cities[b].coord
                    if (i == 0) {
                        paper.path(['M', x1, y1, 'L', x2, y2]).attr(attr.line.normal)
                    }
                    line_dict[a+b] = paper.path(['M', x1, y1, 'L', x1, y1]).attr(attr.line.power)
                }
            }

            /*----------------------------------------------*
             *
             * draw city circles
             *
             *----------------------------------------------*/
            for (const city in cities) {
                const [cx, cy] = cities[city].coord
                cities[city]['circle'] = paper.circle( cx, cy, RADIUS).attr(attr.city.normal)
                paper.text(cx, cy, city).attr(attr.text.city)
            }

            /*----------------------------------------------*
             *
             * start power supply
             *
             *----------------------------------------------*/
            if (result_addon_01 == 'Fail') {
                return
            }

            let tgt_cities = Object.keys(power_plants)
            let next_cities = Object.keys(power_plants)

            // #1 prepare power plant
            let first = true
            for (const city in power_plants) {
                cities[city].circle.animate(attr.city.plant, DELAY)
                const [cx, cy] = cities[city].coord
                paper.text(cx+8, cy-6, cities[city].power).attr(attr.text.power)
                first = false
            }

            power_supply()

            // #2 power supply

            function power_supply() {

                if (next_cities.length == 0) {
                    return
                }

                tgt_cities = next_cities.slice()
                next_cities = []

                for (let tgt of tgt_cities) {
                    const tgt_city = cities[tgt]
                    if (tgt_city.power > 0) {
                        for (let next of tgt_city.net) {
                            const next_city = cities[next]
                            if (next_city.power == 0 || next_city.power < tgt_city.power-1) {
                                next_city.power = tgt_city.power-1
                                next_cities.push(next)
                            }
                        }
                    }
                }

                extend_lines()

                function extend_lines() {
                    let first = true
                    for (let tgt_city of tgt_cities) {
                        if (cities[tgt_city].power == 0) {
                            continue
                        }
                        for (next_city of cities[tgt_city].net) {
                            if (tgt_city+next_city in line_dict) {
                                const m = ['M'].concat(cities[tgt_city].coord)
                                const l = ['L'].concat(cities[next_city].coord)
                                line_dict[tgt_city+next_city].animate(
                                    {'path': m.concat(l)},
                                    DELAY*1.2,
                                    first ? powered_cities: ()=>{}
                                )
                            }
                            first = false
                        }
                    }
                }

                function powered_cities() {
                    const next_cities_set = new Set(next_cities)
                    for (let next_city of next_cities_set) {
                        cities[next_city].circle.animate(attr.city.powered, DELAY*1.5)
                    }
                    power_supply()
                }
            }

        }
        var $tryit;
        var io = new extIO({
            functions: {
                js: 'powerPlants',
                python: 'power_plants'
            },
            multipleArguments: true,
            animation: function($expl, data){
                powerPlantsCanvas(
                    $expl[0],
                    data);
            }
        });
        io.start();
    }
);
