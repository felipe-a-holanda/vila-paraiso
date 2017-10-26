$(function() {
	window.scrollReveal = new scrollReveal();
	"use strict";
	
	// PreLoader
	$(window).load(function() {
		$(".loader").fadeOut(400);
	});

	// Backstretchs
	$("#header").backstretch(background_url);
	$("#services").backstretch(background_url_2);
	
	// Countdown
	$('.countdown').downCount({
		date: '12/12/2017 12:00:00',
		offset: +10
	});			
    
});
