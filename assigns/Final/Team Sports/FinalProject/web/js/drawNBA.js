/*
 * BIA 660 Final Project
 *	
 * Author: Han Yan
 */


var b_attr = ['G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'BLK', 'TOV', 'PF', 'PTS', 'PTS/G'];
var attr_names = {'G': 'Games', 'TRB':'Total Rebounds', 'MP': 'Minutes Played', 'FG':'Field Goals', 'FGA':'Field Goal Attempts', 'FG%':'Field Goal Percentage', '3P':'3-Point Field Goals', '3PA':'3-Point Field Goal Attempts', '3P%': '3-Point Field Goal Percentage', 'FT':'Free Throws', 'FTA':'Free Throw Attempts', 'FT%':'Free Throw Percentage', 'ORB':'Offensive Rebounds', 'DRB':'Defensive Rebounds', 'AST':'Assists', 'BLK':'Blocks', 'TOV':'Turnovers', 'PF':'Personal Fouls', 'PTS':'Points', 'PTS/G':'Points Per Game'};

var adv_attr = ['Age', 'O_eFG%', 'O_TOV%', 'O_ORB%', 'O_FT/FGA'];
var adv_attr_names = {'Age':'Age', 'O_eFG%':'Effective Field Goal Percentage','O_TOV%':'Turnover Percentage', 'O_ORB%':'Offensive Rebound Percentage', 'O_FT/FGA':'Free Throws Per Field Goal Attempt'};

var final_attr = ['FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL','BLK', 'TOV', 'PF', 'PTS']


function drawNBABasicStats(request_attr, div_id){
	var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/basketball/regularstatus?team=League%20Average&attribute=" + request_attr + "&year=0&order=1";
	var years = [];
	var attr_data = [];
    $.getJSON(url, function(json) {
    	$.each(json, function(key, val) {
    		years.push(val.year);
    		attr_data.push(val[request_attr]);
		});
		$('#'+div_id).highcharts({
            chart: {
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: 'Basic Statistics: ' + attr_names[request_attr] + " 2001-2013",
                x: -20 //center
            },
            subtitle: {
                text: '',
                x: -20
            },
            xAxis: {
                categories: years
            },
            yAxis: {
                title: {
                    text: ''
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ''
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: [{
                name: request_attr,
                data: attr_data
            }]
        });
    });
}

function drawNBAAdvancedStats(adv_request_attr, div_id){
	var adv_request_attr = $('#adv-attr-select').val();
	var adv_url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999/basketball/misstatus?team=League%20Average&attribute=" + adv_request_attr + "&year=0&order=1";
	var adv_years = [];
	var adv_attr_data = [];
	console.log(adv_attr_names['O_TOV%']);
    $.getJSON(adv_url, function(json) {
    	$.each(json, function(key, val) {
    		adv_years.push(val.year);
    		adv_attr_data.push(val[adv_request_attr]);
		});
		$('#'+div_id).highcharts({
            chart: {
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: 'Advanced Statistics: ' + adv_attr_names[adv_request_attr] + " 2001-2013",
                x: -20 //center
            },
            subtitle: {
                text: '',
                x: -20
            },
            xAxis: {
                categories: adv_years
            },
            yAxis: {
                title: {
                    text: ''
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ''
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: [{
                name: adv_request_attr,
                data: adv_attr_data
            }]
        });
    });
}


function drawFinalTotalScores(div_id) {
	url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999//basketball/finalTotals?team=champion";
	var eachTotal = [];
	var yearData=[];
	var notChampionTotal = [];
	$.getJSON(url, function(json) {
		$.each(json, function(key, val) {
			for (var i = 2001; i < 2013; i++) {
				yearData.push(i);
			}
			eachTotal.push(val);
		});
			url2 = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999//basketball/finalTotals?team=nochampion";
			$.getJSON(url2, function(json) {
	        	$.each(json, function(key, val) {
					notChampionTotal.push(val);
				});
				$('#'+div_id).highcharts({
	            chart: {
	                type: 'line',
	                marginRight: 130,
	                marginBottom: 25
	            },
	            title: {
	                text: 'NBA Final Game Total Scores(2001-2013)',
	                x: -20 //center
	            },
	            subtitle: {
	                text: '',
	                x: -20
	            },
	            xAxis: {
	                categories: yearData
	            },
	            yAxis: {
	                title: {
	                    text: ''
	                },
	                plotLines: [{
	                    value: 0,
	                    width: 1,
	                    color: '#808080'
	                }]
	            },
	            tooltip: {
	                valueSuffix: ''
	            },
	            legend: {
	                layout: 'vertical',
	                align: 'right',
	                verticalAlign: 'top',
	                x: -10,
	                y: 100,
	                borderWidth: 0
	            },
	            series: [{
	                name: 'Champion',
	                data: eachTotal
	            	},
	            	{
	                name: 'Non-champion',
	                data: notChampionTotal
	            	}	
	            ]
	        });
		});
	});
}

function drawNBAFinalEachStats(request_attr, div_id){
	var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999//basketball/finalEachStatus?attribute=" + request_attr;
    $.getJSON(url, function(json) {
    	var championData = json['Champion']
    	var notChampionData = json['NotChampion']
		$('#'+div_id).highcharts({
            chart: {
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: 'Final Game Basic Statistics:' + ' ' + attr_names[request_attr] + ' 2001 - 2012',
                x: -20 //center
            },
            subtitle: {
                text: '',
                x: -20
            },
            xAxis: {
                categories: [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
            },
            yAxis: {
                title: {
                    text: ''
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ''
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: [{
	                name: 'Champion',
	                data: championData
	            	},
	            	{
	                name: 'Non-champion',
	                data: notChampionData
	            	}	
			]
        });
    });
}

function drawNBAFinalQuarter(request_attr, div_id){
	var url = "http://ec2-54-234-59-234.compute-1.amazonaws.com:9999//basketball/finalQuarter?quarter=" + request_attr;
    $.getJSON(url, function(json) {
    	var championData = json['Champion']
    	var notChampionData = json['NotChampion']
		$('#'+div_id).highcharts({
            chart: {
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: 'Final Game Quarter Scores' + ' 2001 - 2012',
                x: -20 //center
            },
            subtitle: {
                text: '',
                x: -20
            },
            xAxis: {
                categories: [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
            },
            yAxis: {
                title: {
                    text: ''
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ''
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: [{
	                name: 'Champion',
	                data: championData
	            	},
	            	{
	                name: 'Non-champion',
	                data: notChampionData
	            	}	
			]
        });
    });
}
