// loading screen
$(window).load(function () {
	$('#loading').fadeOut('slow');
});

// toggle back and forth
jQuery(function( $ ){

	$('div.pane').scrollTo( 0 );

	$.scrollTo( 0 );
	
	var regions = $('section');
	var active_region = 0, prev, next;
		
	function setup_region ()
	{
		if ( active_region == 0 )
		{
			$('#toggle .previous a').fadeOut('slow');
			prev = regions.size() - 1;	
		}
		else
		{
			$('#toggle .previous a').fadeIn('slow');
			prev = active_region - 1;	
		}
		
		if ( active_region == ( regions.size() - 1 ) )
		{
			$('#toggle .next a').fadeOut('slow');
			next = 0;
		}
		else
		{
			$('#toggle .next a').fadeIn('slow');
			next = active_region+1;	
		}
				
		$('#toggle .previous a').attr('href', '#'+ $(regions).eq(prev).attr('id')).click(function(){ active_region = prev; });
		$('#toggle .next a').attr('href', '#'+ $(regions).eq(next).attr('id')).click(function(){ active_region = next; });
	}
	setup_region();
	
	$('#toggle a').click(function(){

	$.scrollTo( this.hash, 1500, {center:true});
	setup_region();

	return false; 

	});
});

// portfolio scrollable gallery
function makeScrollable(wrapper, scrollable){

	var wrapper = $(wrapper), scrollable = $(scrollable);

	scrollable.hide();
	var loading = $('<div class="loading">Loading...</div>').appendTo(wrapper);

	var interval = setInterval(function(){
		var images = scrollable.find('img');
		var completed = 0;

		images.each(function(){
			if (this.complete) completed++;
		});

		if (completed == images.length){
			clearInterval(interval);

			setTimeout(function(){

				loading.hide();

				wrapper.css({overflow: 'hidden'});

				scrollable.slideDown('slow', function(){
					enable();
				});
			}, 1000);
		}
	}, 100);

	function enable(){
		var inactiveMargin = 99;
		var wrapperWidth = wrapper.width();
		var wrapperHeight = wrapper.height();
		var scrollableHeight = scrollable.outerHeight() + 2*inactiveMargin;

		var lastTarget;
		wrapper.mousemove(function(e){
		lastTarget = e.target;

		var wrapperOffset = wrapper.offset();

		var top = (e.pageY -  wrapperOffset.top) * (scrollableHeight - wrapperHeight) / wrapperHeight - inactiveMargin;
		if (top < 0){
			top = 0;
		}
		wrapper.scrollTop(top);
	});

	}

}
$(function(){
	makeScrollable("div.sc_menu_wrapper", "div.sc_menu");
});

// horizontal scrolling
;(function( $ ){
	
	var $scrollTo = $.scrollTo = function( target, duration, settings ){
		$(window).scrollTo( target, duration, settings );
	};

	$scrollTo.defaults = {
		axis:'xy',
		duration: parseFloat($.fn.jquery) >= 1.3 ? 0 : 1
	};

	$scrollTo.window = function( scope ){
		return $(window)._scrollable();
	};

	$.fn._scrollable = function(){
		return this.map(function(){
			var elem = this,
				isWin = !elem.nodeName || $.inArray( elem.nodeName.toLowerCase(), ['iframe','#document','html','body'] ) != -1;

				if( !isWin )
					return elem;

			var doc = (elem.contentWindow || elem).document || elem.ownerDocument || elem;
			
			return $.browser.safari || doc.compatMode == 'BackCompat' ?
				doc.body : 
				doc.documentElement;
		});
	};

	$.fn.scrollTo = function( target, duration, settings ){
		if( typeof duration == 'object' ){
			settings = duration;
			duration = 0;
		}
		if( typeof settings == 'function' )
			settings = { onAfter:settings };
			
		if( target == 'max' )
			target = 9e9;
			
		settings = $.extend( {}, $scrollTo.defaults, settings );

		duration = duration || settings.speed || settings.duration;

		settings.queue = settings.queue && settings.axis.length > 1;
		
		if( settings.queue )

			duration /= 2;
		settings.offset = both( settings.offset );
		settings.over = both( settings.over );

		return this._scrollable().each(function(){
			var elem = this,
				$elem = $(elem),
				targ = target, toff, attr = {},
				win = $elem.is('html,body');

			switch( typeof targ ){

				case 'number':
				case 'string':
					if( /^([+-]=)?\d+(\.\d+)?(px|%)?$/.test(targ) ){
						targ = both( targ );
						break;
					}

					targ = $(targ,this);
				case 'object':

					if( targ.is || targ.style )

						toff = (targ = $(targ)).offset();
			}
			$.each( settings.axis.split(''), function( i, axis ){
				var Pos	= axis == 'x' ? 'Left' : 'Top',
					pos = Pos.toLowerCase(),
					key = 'scroll' + Pos,
					old = elem[key],
					max = $scrollTo.max(elem, axis);

				if( toff ){
					attr[key] = toff[pos] + ( win ? 0 : old - $elem.offset()[pos] );

					if( settings.margin ){
						attr[key] -= parseInt(targ.css('margin'+Pos)) || 0;
						attr[key] -= parseInt(targ.css('border'+Pos+'Width')) || 0;
					}
					
					attr[key] += settings.offset[pos] || 0;
					
					if (settings.center) {
					var dimKey = axis== 'x' ? 'width' : 'height';
					attr[key] -= ($elem[dimKey]() - targ[dimKey]()) / 2;
					}
					
					if( settings.over[pos] )

						attr[key] += targ[axis=='x'?'width':'height']() * settings.over[pos];
				}else{ 
					var val = targ[pos];

					attr[key] = val.slice && val.slice(-1) == '%' ? 
						parseFloat(val) / 100 * max
						: val;
				}

				if( /^\d+$/.test(attr[key]) )

					attr[key] = attr[key] <= 0 ? 0 : Math.min( attr[key], max );

				if( !i && settings.queue ){

					if( old != attr[key] )

						animate( settings.onAfterFirst );

					delete attr[key];
				}
			});

			animate( settings.onAfter );			

			function animate( callback ){
				$elem.animate( attr, duration, settings.easing, callback && function(){
					callback.call(this, target, settings);
				});
			};

		}).end();
	};
	
	$scrollTo.max = function( elem, axis ){
		var Dim = axis == 'x' ? 'Width' : 'Height',
			scroll = 'scroll'+Dim;
		
		if( !$(elem).is('html,body') )
			return elem[scroll] - $(elem)[Dim.toLowerCase()]();
		
		var size = 'client' + Dim,
			html = elem.ownerDocument.documentElement,
			body = elem.ownerDocument.body;

		return Math.max( html[scroll], body[scroll] ) 
			 - Math.min( html[size]  , body[size]   );
			
	};

	function both( val ){
		return typeof val == 'object' ? val : { top:val, left:val };
	};

})( jQuery );
