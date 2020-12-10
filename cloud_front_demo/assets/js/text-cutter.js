// START READ MORE TEXT CUTTER
function textCutter(i, text) {
  var short = text.substr(0, i);
  if (/^\S/.test(text.substr(i)))
    return short.replace(/\s+\S*$/, "") + "...";
  return short + "...";
};

/* Slick has an issue with adaptiveHeight when one object is present.
  Set adaptiveHeight to false when only one instance of the object exists. */
  var testimonialAdaptiveHeight = true;

  let testimonialSlider = $(".testimonial-slider .text");

  function sliderCutter(sliderName, details, txtLength, link=false) {
    sliderName.each(function(idx, slider) {
      if ($(this).html().length > txtLength) {
        $(this).data(`${details}-details`, $(this).html());
        $(this).data("max", $(this).height());
        $(this).html(textCutter(txtLength, $(this).data(`${details}-details`)));
        $(this).data("min", $(this).height());
        $(this).css({ height: '100%' });
        if(link==false) {
          $(this).after("<span class='read-more'>read more</span>");
        }
        var more = $(this).siblings('.read-more');
        var SELF = this;
        $(more).click(function() {
          $(SELF).toggleClass(`open-${details}`);
          if ($(SELF).hasClass(`open-${details}`)) {
            $(SELF).html($(SELF).data(`${details}-details`));
            $(SELF).animate({ height: '100%' }, 300);
            $(more).text("read less");
            $('.testimonial-slider').slick('refresh');
          } else {
            $(SELF).animate({ height: '100%' }, 300, function () {
              $(this).html(textCutter(txtLength, $(SELF).data(`${details}-details`)));
              $(more).text("read more");
              $('.testimonial-slider').slick('refresh');
            })
          }
        })
      }
    })
  }

  sliderCutter(testimonialSlider, "testimonials", 210);
