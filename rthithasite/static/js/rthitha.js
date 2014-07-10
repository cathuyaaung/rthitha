$(document).ready(function(){

	//bind methods
	$(function() {
		$('.comment-form form').bindPostCommentHandler();
		$('.reply-show-hide-form').bindCommentFormShowHideHandler();
		$('.comment-form-btn-cancel').bindCommentFormCancelHandler();
		$('.movielink').bindShowPlayer();
	});

	(function( $ ){
	$.fn.bindShowPlayer = function() {

		$('div.location').each(function() {
			var $locationdiv = $(this)

			$("a.movielink", $locationdiv).click(function(e) {
                var id = $(this).attr('id');
                var target = $(this).attr('target');

      var d = $(this).data('srt');
      alert(d);
      var subtitles1 = d;

				if($(document).find('.targetlocation').length){
					$targetlocation = $('.targetlocation');

					if(id==1){
					    strHtml = "<iframe id='f' name='widget' src='"+target+
                        "' width='852' height='510' style='float:center'></iframe>";
                        $targetlocation.html(strHtml);
					}else{

					    strHtml = "<video width='852' height='510' controls><source src='"+target+
                        "'><track kind='captions' srclang='en' label='English'"+
                        "src='"+subtitles1+"' default></track></video>";

                        $targetlocation.html(strHtml);
					}
				}
			});
		});

		$(document).on('click', '.reply-show-hide-form', function(){
			$('.comment-form').hide();
			$('#'+$(this).attr('target')).show();
		});
		};
	})( jQuery );


	(function( $ ){
	$.fn.bindCommentFormCancelHandler = function() {

	//control to show hide comment form when clicked on cancel
		$('div.comment-form').each(function() {
			var $commentform = $(this)

			$("button.comment-form-btn-cancel", $commentform).click(function(e) {
				e.preventDefault();
				$commentform.toggle();
				$("div.comment-form").not($commentform).hide();
				return false;
			});
		});


		};
	})( jQuery );

	//control to show hide comment forms when clicked on 'reply' 'post comment'
	//$('.reply-show-hide-form').click(function(){
	(function( $ ){
	$.fn.bindCommentFormShowHideHandler = function() {
		$(document).on('click', '.reply-show-hide-form', function(){
			$('.comment-form').hide();
			$('#'+$(this).attr('target')).show();
		});
		};
	})( jQuery );



	(function( $ ){
	$.fn.bindPostCommentHandler = function() {
		// We get passed a list of forms; iterate and get a unique id for each
		// attach a submit trigger to handle saving and returning
		this.each(function() {
			//$(this).find('input.submit-preview').remove();
			$(this).submit(function() {
				commentform = this;
				commentformdiv = $(this).parent();
				var comment_text = $('#id_comment').val();

				$.ajax({
					type: "POST",
					data: $(commentform).serialize(),
					url: "/comments/post/",
					cache: false,
					dataType: "html",
					success: function(html, textStatus) {
						//alert(html);


						$(commentformdiv).hide();

						//if($('#parent_id').length){
						if($(commentformdiv).find('#parent_id').length){

							//replying comment

							$commentbodydiv = commentformdiv.parent();
							if($commentbodydiv.find('.comment-children').length){
								$childrenul = $commentbodydiv.find('.comment-children');
							}else{
								var $childrenul = $("<ul>", {id: "foo", class: "comment-children"});
								$childrenul.appendTo($commentbodydiv);
							}
							var li = $('<li>').prependTo($childrenul);
							$(html).appendTo(li).fadeIn(500);


						}else{


							//root
							if($(document).find('.comment-root').length){
								$commentroot = $('.comment-root');
								$commentroot.prepend($('<div>').append($('<li>').append(html)));
							}
							else{
								var paneldiv = $('<div>', {class:"panel"});
								paneldiv.insertAfter(commentformdiv);

								var rootul =  $('<ul>', {class:"comment-root"}).appendTo(paneldiv);
								var div =  $('<div>').appendTo(rootul);
								var li = $('<li>').appendTo(div);
								$(html).appendTo(li);
							}



						}



						$(html).find('.reply-show-hide-form').bindCommentFormShowHideHandler();
						$(html).find('.comment-form-btn-cancel').bindCommentFormCancelHandler();
						$(html).find('.comment-form form').bindPostCommentHandler();
					},
					error: function (XMLHttpRequest, textStatus, errorThrown) {
						$(commentform).replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.'+textStatus+errorThrown);
					}
				});
				return false;
			});
		}); //each
	};
	})( jQuery );

	if (window.location.hash == '#_=_') {
      window.location.hash = '';
   }

});