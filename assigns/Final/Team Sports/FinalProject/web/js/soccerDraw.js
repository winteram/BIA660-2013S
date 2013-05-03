
/*
 * BIA 660 Final Project
 *
 * Author: Sen yang
 */



// --------------------------England Premier League--------------------------
//G1: line chart: 2002 to 2012 Home and Away Total Goals
function drawLineEngTotalGoals() {
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=2002%20to%202012%20Home%20and%20Away%20Total%20Goals";
    var categories = [];
    var dataHGS = [];
    var dataAGS = [];
    var dataTotal = [];
    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        //"Charlton Athletic": {"Home Goals Conceded per Game": 1.5789473684210527, "Away Goals Conceded per Game": 1.368421052631579},
        $.each(json, function (key, val) {
            var hg = parseFloat(val["Home Goals Scored"]);
            var ag = parseFloat(val["Away Goals Scored"]);
            var total = hg + ag;
            categories.push(key);
            dataHGS.push(hg);
            dataAGS.push(ag);
            dataTotal.push(total);
        });

        var divId = "EHATG";
        var titleText = 'England Premier League 2002 to 2012 Home and Away Total Goals';
        var hgsName = 'Home Goals Scored';
        var agsName = 'Away Goals Scored';
        var totalName = 'Total Goals Scored';
        var hgsColor = '#FF0000';
        var agsColor = '#2E9AFE';
        var totalColor = "green";

        // draw chart based on options
        var options = lineOption(divId, categories, titleText, hgsName, dataHGS, hgsColor,
            agsName, dataAGS, agsColor, totalName, dataTotal, totalColor);
        var chart = new Highcharts.Chart(options);

    });
}


// G2: bar chart: Home and Away Goals Conceded per Game per Season
function drawBarHAC(year) {
    // Build  categories, bar 1 Data ,bar 2 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=Home%20and%20Away%20Goals%20Conceded%20per%20Game%20per%20Season&year=" + year;
    var categories = [];
    var b1Data = [];
    var b2Data = [];

    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        //"Charlton Athletic": {"Home Goals Conceded per Game": 1.5789473684210527, "Away Goals Conceded per Game": 1.368421052631579},
        $.each(json, function (key, val) {
            var hg = parseFloat(parseFloat(val["Home Goals Conceded per Game"]).toFixed(2));
            var ag = parseFloat(parseFloat(val["Away Goals Conceded per Game"]).toFixed(2));
            categories.push(key);
            b1Data.push(hg);
            b2Data.push(ag);
        });

        var divId = "HAC";
        var titleText = 'Home and Away Goals Conceded per Game per Season ' + year;
        var b1Name = 'Home Goals Conceded per Game';
        var b2Name = 'Away Goals Conceded per Game';
        var b1Color = '#FF0000';
        var b2Color = '#2E9AFE';

        var options = createOption(divId, categories, titleText, b1Name, b1Data, b1Color, b2Name, b2Data, b2Color);
        var chart = new Highcharts.Chart(options);

    });
}


// G3: Home and Away Goals Scored per Game per Season
function drawBarHAS(year) {
    // Build  categories, bar 1 Data ,bar 2 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=Home%20and%20Away%20Goals%20Scored%20per%20Game%20per%20Season&year=" + year;
    var categories = [];
    var b1Data = [];
    var b2Data = [];

    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        //"Charlton Athletic": {"Home Goals Scored per Game": 1.5789473684210527, "Away Goals Scored per Game": 1.368421052631579},
        $.each(json, function (key, val) {
            var hg = parseFloat(parseFloat(val["Home Goals Scored per Game"]).toFixed(2));
            var ag = parseFloat(parseFloat(val["Away Goals Scored per Game"]).toFixed(2));
            categories.push(key);
            b1Data.push(hg);
            b2Data.push(ag);
        });

        var divId = "HAS";
        var titleText = 'Home and Away Goals Scored per Game per Season ' + year;
        var b1Name = 'Home Goals Scored per Game';
        var b2Name = 'Away Goals Scored per Game';
        var b1Color = '#31B404';
        var b2Color = 'black';

        var options = createOption(divId, categories, titleText, b1Name, b1Data, b1Color, b2Name, b2Data, b2Color);
        var chart = new Highcharts.Chart(options);

    });
}
//G5: Goals Difference
function drawVBarEnGoalsDiff(year) {
    // Build  categories, bar 1 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?chartName=Goal%20Different&year=" + year;
    var categories = [];
    var b1Data = [];


    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            categories.push(key);
            var score = parseFloat(val["Goal Different"]);
            b1Data.push(score);
        });

        var divId = "EGD";
        var titleText = 'Goal Difference ' + year;
        var b1Name = 'Goal Difference';
        var b1Color = 'orange';

        var options = verticalBarChart(divId, categories, titleText, b1Name, b1Data, b1Color);
        var chart = new Highcharts.Chart(options);

    });
}
//G6:   Goals Scored and Goals Conceded per Team per Season
function drawVBarEnGoalsSC(year) {
    // Build  categories, bar 1 Data , bar2 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=Goals%20Scored%20and%20Goals%20Conceded%20per%20Team%20per%20Season&year=" + year;
    var categories = [];
    var b1Data = [];
    var b2Data = [];


    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            categories.push(key);
            var gc = parseFloat(val["Goals Conceded"]);
            var gs = parseFloat(val["Goals Scored"]);
            b1Data.push(gc);
            b2Data.push(gs);
        });

        var divId = "EGSGC";
        var titleText = 'Goals Scored and Goals Conceded per Team per Season ' + year;
        var b1Name = 'Goals Conceded';
        var b2Name = 'Goals Scored';
        var b1Color = 'blue';
        var b2Color = '#E74C3C';

        var options = verticalTwoBarChart(divId, categories, titleText, b1Name, b1Data, b1Color, b2Name, b2Data, b2Color);
        var chart = new Highcharts.Chart(options);

    });
}
//G7:
function drawLineEngGSTT() {
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=2002%20to%202012%20Goals%20Scored%20of%20Top%20Team";
    var categories = [];
    var dataGS = [];
    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        //"Charlton Athletic": {"Home Goals Conceded per Game": 1.5789473684210527, "Away Goals Conceded per Game": 1.368421052631579},
        $.each(json, function (key, val) {
            var gs = parseFloat(val["Goals Scored"]);
            categories.push(key);
            dataGS.push(gs);

        });

        var divId = "EGSTT";
        var titleText = 'England Premier League 2002 to 2012 Goals Scored of Top Team';
        var hgsName = 'Goals Scored';
        var hgsColor = '#FF0000';
        // draw chart based on options
        var options = lineOptionSingle(divId, categories, titleText, hgsName, dataGS, hgsColor);
        var chart = new Highcharts.Chart(options);

    });
}

//G8: 2002 to 2012 Home Goals Scored of Top Team

function drawLineEHGSTP(){

    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=2002%20to%202012%20Home%20Goals%20Scored%20of%20Top%20Team";
    var categories = [];
    var dataGS = [];
    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            var gs = parseFloat(val["Home Goals Scored"]);
            categories.push(key);
            dataGS.push(gs);

        });

        var divId = "EHGSTP";
        var titleText = 'England Premier League 2002 to 2012 Home Goals Scored of Top Team';
        var hgsName = 'Home Goals Scored';
        var hgsColor = '#FF0000';
        // draw chart based on options
        var options = lineOptionSingle(divId, categories, titleText, hgsName, dataGS, hgsColor);
        var chart = new Highcharts.Chart(options);

    });
}

//G9: 2002 to 2012 Pts of Top Team
function drawBarEPtsTT(){
    // Build  categories, bar 1 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=2002%20to%202012%20Pts%20of%20Top%20Team";
    var categories = [];
    var b1Data = [];


    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            categories.push(key);
            var score = parseFloat(val["Pts"]);
            b1Data.push(score);
        });

        var divId = "EPtsTT";
        var titleText = "2002 to 2012 Pts of Top Team";
        var b1Name = 'Pts';
        var b1Color = 'green';

        var options = verticalBarChart(divId, categories, titleText, b1Name, b1Data, b1Color);
        var chart = new Highcharts.Chart(options);

    });
}

//G10: 2002 to 2012 Won Home of Top Team
function drawLineEWHTT(){

    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=2002%20to%202012%20Won%20Home%20of%20Top%20Team";
    var categories = [];
    var dataGS = [];
    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            var gs = parseFloat(val["Won Home"]);
            categories.push(key);
            dataGS.push(gs);

        });

        var divId = "EWHTT";
        var titleText = 'England Premier League 2002 to 2012 Won Home of Top Team';
        var hgsName = 'Won Home';
        var hgsColor = '#FF0000';
        // draw chart based on options
        var options = lineOptionSingle(divId, categories, titleText, hgsName, dataGS, hgsColor);
        var chart = new Highcharts.Chart(options);

    });
}

//G11: 2002 to 2012 Won of Top Team
function drawBarEWTT(){
    // Build  categories, bar 1 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=2002%20to%202012%20Won%20of%20Top%20Team";
    var categories = [];
    var b1Data = [];


    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            categories.push(key);
            var score = parseFloat(val["Won"]);
            b1Data.push(score);
        });

        var divId = "EWTT";
        var titleText = "2002 to 2012 Won of Top Team";
        var b1Name = 'Won';
        var b1Color = 'Blue';

        var options = verticalBarChart(divId, categories, titleText, b1Name, b1Data, b1Color);
        var chart = new Highcharts.Chart(options);

    });
}

// --------------------------Spanish Premier League--------------------------
//G1: line chart: 2002 to 2012 Home and Away Total Goals
function drawLineSpanTotalGoals() {
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?chartName=goals_sum";
    var categories = [];
    var dataHGS = [];
    var dataAGS = [];
    var dataTotal = [];
    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        //"Charlton Athletic": {"Home Goals Conceded per Game": 1.5789473684210527, "Away Goals Conceded per Game": 1.368421052631579},
        $.each(json, function (key, val) {
            var hg = parseFloat(val["HGS"]);
            var ag = parseFloat(val["AGS"]);
            var total = parseFloat(val["TGS"]);
            categories.push(key);
            dataHGS.push(hg);
            dataAGS.push(ag);
            dataTotal.push(total);
        });

        var divId = "SHATG";
        var titleText = 'Spanish Premier League 2003 to 2011 Home and Away Total Goals';
        var hgsName = 'Home Goals Scored';
        var agsName = 'Away Goals Scored';
        var totalName = 'Total Goals Scored';
        var hgsColor = '#FF0000';
        var agsColor = '#2E9AFE';
        var totalColor = "green";

        // draw chart based on options
        var options = lineOption(divId, categories, titleText, hgsName, dataHGS, hgsColor,
            agsName, dataAGS, agsColor, totalName, dataTotal, totalColor);
        var chart = new Highcharts.Chart(options);

    });
}

//G2: rate_against
function drawBarRateAgainst(season) {
    // Build  categories, bar 1 Data ,bar 2 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=rate_against&season=" + season;
    var categories = [];
    var b1Data = [];
    var b2Data = [];

    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            var hg = parseFloat(parseFloat(val["HGCpG"]).toFixed(2));//Home Goals Conceded per Game
            var ag = parseFloat(parseFloat(val["AGCpG"]).toFixed(2));//Away Goals Conceded per Game
            categories.push(key);
            b1Data.push(hg);
            b2Data.push(ag);
        });

        var divId = "SHAC";
        var titleText = 'Home and Away Goals Conceded per Game per Season ' + season;
        var b1Name = 'Home Goals Conceded per Game';
        var b2Name = 'Away Goals Conceded per Game';
        var b1Color = '#FF0000';
        var b2Color = '#2E9AFE';

        var options = createOption(divId, categories, titleText, b1Name, b1Data, b1Color, b2Name, b2Data, b2Color);
        var chart = new Highcharts.Chart(options);

    });
}

//G3: rate_scored
function drawBarRateScored(season) {
    // Build  categories, bar 1 Data ,bar 2 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?chartName=rate_scored&season=" + season;
    var categories = [];
    var b1Data = [];
    var b2Data = [];

    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            var hg = parseFloat(parseFloat(val["HGSpG"]).toFixed(2));//Home Goals Scored per Game
            var ag = parseFloat(parseFloat(val["AGSpG"]).toFixed(2));//Away Goals Scored per Game
            categories.push(key);
            b1Data.push(hg);
            b2Data.push(ag);
        });

        var divId = "SHAS";
        var titleText = 'Home and Away Goals Scored per Game per Season ' + season;
        var b1Name = 'Home Goals Scored per Game';
        var b2Name = 'Away Goals Scored per Game';
        var b1Color = '#31B404';
        var b2Color = 'black';

        var options = createOption(divId, categories, titleText, b1Name, b1Data, b1Color, b2Name, b2Data, b2Color);
        var chart = new Highcharts.Chart(options);

    });
}

//G5: Goals Difference
function drawVBarSpGoalsDiff(season) {
    // Build  categories, bar 1 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?chartName=goal_difference&season=" + season;
    var categories = [];
    var b1Data = [];


    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            categories.push(key);
            b1Data.push(val);
        });

        var divId = "SGD";
        var titleText = 'Goal Difference ' + season;
        var b1Name = 'Goal Difference';
        var b1Color = '#31B404';

        var options = verticalBarChart(divId, categories, titleText, b1Name, b1Data, b1Color);
        var chart = new Highcharts.Chart(options);

    });
}

//G6:   Goals Scored and Goals Conceded per Team per Season
function drawVBarSpanSA(season) {
    // Build  categories, bar 1 Data , bar2 Data
    var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/football/premierleague?" +
        "chartName=goal_scored_against&season=" + season;
    var categories = [];
    var b1Data = [];
    var b2Data = [];


    $.getJSON(url, function (json) {
        // json objects example: key = team name; val = ...
        $.each(json, function (key, val) {
            categories.push(key);
            var gc = parseFloat(val["GC"]);
            var gs = parseFloat(val["GS"]);
            b1Data.push(gc);
            b2Data.push(gs);
        });

        var divId = "SGCS";
        var titleText = 'Goals Scored and Goals Conceded per Team per Season ' + season;
        var b1Name = 'Goals Conceded';
        var b2Name = 'Goals Scored';
        var b1Color = 'green';
        var b2Color = 'orange';

        var options = verticalTwoBarChart(divId, categories, titleText, b1Name, b1Data, b1Color, b2Name, b2Data, b2Color);
        var chart = new Highcharts.Chart(options);

    });
}



// bar chart options
function createOption(divId, categories, titleText, b1Name, b1Data, b1Color, b2Name, b2Data, b2Color) {
    return {
        chart: {
            renderTo: divId,
            type: 'bar'
        },
        title: {
            text: titleText
        },
        subtitle: {
            text: 'Source: web'
        },
        xAxis: {
            categories: categories,
            title: {
                text: "Team Name"
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Home and Away Goals',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ''
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                },
                pointWidth: 10
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -100,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: '#FFFFFF',
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [
            {
                name: b1Name,
                data: b1Data,
                color: b1Color
            },
            {
                name: b2Name,
                data: b2Data,
                color: b2Color
            }
        ]
    }
}

// line option
function lineOption(divId, categories, titleText, d1Name, d1Data, d1Color, d2Name, d2Data, d2Color, d3Name, d3Data, d3Color) {
    return {
        chart: {
            renderTo: divId,
            type: 'line',
            marginRight: 130,
            marginBottom: 25
        },
        title: {
            text: titleText,
            x: -20 //center
        },
        subtitle: {
            text: 'Source: Web',
            x: -20
        },
        xAxis: {
            categories: categories,
            title: {
                text: "Year",
                align: 'high'
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Scores'
            },
            plotLines: [
                {
                    value: 0,
                    width: 1,
                    color: '#808080'
                }
            ]
        },
        // showing the scores
//        tooltip: {
////            valueSuffix: '',
//            enabled: false,
//            formatter: function() {
//                return '<b>'+ this.series.name +'</b><br/>'+
//                    this.x +': '+ this.y;
//            }
//        },
//        plotOptions: {
//            line: {
//                dataLabels: {
//                    enabled: true
//                },
//                enableMouseTracking: false
//            }
//        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -10,
            y: 100,
            borderWidth: 0
        },
        series: [
            {
                name: d1Name,
                data: d1Data,
                color: d1Color
            },
            {
                name: d2Name,
                data: d2Data,
                color: d2Color
            },
            {
                name: d3Name,
                data: d3Data,
                color: d3Color
            }
        ]
    }
}

// line option
function lineOptionSingle(divId, categories, titleText, d1Name, d1Data, d1Color) {
    return {
        chart: {
            renderTo: divId,
            type: 'line',
            marginRight: 130,
            marginBottom: 25
        },
        title: {
            text: titleText,
            x: -20 //center
        },
        subtitle: {
            text: 'Source: Web',
            x: -20
        },
        xAxis: {
            categories: categories,
            title: {
                text: "Year",
                align: 'high'
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Scores'
            },
            plotLines: [
                {
                    value: 0,
                    width: 1,
                    color: '#808080'
                }
            ]
        },
        // showing the scores
//        tooltip: {
////            valueSuffix: '',
//            enabled: false,
//            formatter: function() {
//                return '<b>'+ this.series.name +'</b><br/>'+
//                    this.x +': '+ this.y;
//            }
//        },
//        plotOptions: {
//            line: {
//                dataLabels: {
//                    enabled: true
//                },
//                enableMouseTracking: false
//            }
//        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -10,
            y: 100,
            borderWidth: 0
        },
        series: [
            {
                name: d1Name,
                data: d1Data,
                color: d1Color
            }
        ]
    }
}
// vertical bar options
function verticalBarChart(divId, categories, titleText, d1Name, d1Data, d1Color) {
    return {
        chart: {
            renderTo: divId,
            type: 'column'
        },
        title: {
            text: titleText
        },
        xAxis: {
            categories: categories,
            title: {
                text: "Team Name",
                align: 'high'
            }, 
            labels: {
                rotation: -45,
                align: 'right'
            }

        },
        credits: {
            enabled: false
        },
        series: [
            {
                name: d1Name,
                data: d1Data,
                color: d1Color
            }
        ]
    };
}

function verticalTwoBarChart(divId, categories, titleText, d1Name, d1Data, d1Color, d2Name, d2Data, d2Color) {
    return {
        chart: {
            renderTo: divId,
            type: 'column'
        },
        title: {
            text: titleText
        },
        xAxis: {
            categories: categories,
            title: {
                text: "Team Name",
                align: 'high'
            },
            labels: {
                rotation: -45,
                align: 'right'
            }
        },
        credits: {
            enabled: false
        },
        series: [
            {
                name: d1Name,
                data: d1Data,
                color: d1Color
            },
            {
                name: d2Name,
                data: d2Data,
                color: d2Color
            }
        ]
    };
}






