mw.loader.implement("ext.vector.collapsibleNav",function(){(function(mw,$){"use strict";var map,version;function toggle($element){$.cookie('vector-nav-'+$element.parent().attr('id'),$element.parent().is('.collapsed'),{'expires':30,'path':'/'});$element.parent().toggleClass('expanded').toggleClass('collapsed').find('.body').slideToggle('fast');}map={ltr:{opera:[['>=',9.6]],konqueror:[['>=',4.0]],blackberry:false,ipod:false,iphone:false,ps3:false},rtl:{opera:[['>=',9.6]],konqueror:[['>=',4.0]],blackberry:false,ipod:false,iphone:false,ps3:false}};if(!$.client.test(map)){return true;}version=1;if(mw.config.get('wgCollapsibleNavForceNewVersion')){version=2;}else{if(mw.config.get('wgCollapsibleNavBucketTest')){version=$.cookie('vector-nav-pref-version');if(version===null){version=Math.round(Math.random()+1);$.cookie('vector-nav-pref-version',version,{expires:30,path:'/'});}}}$(function($){var limit,threshold,languages,acceptLangCookie,$primary,$secondary,i,$link,count,$headings,tabIndex;if(
version===2){limit=5;threshold=3;$('#p-lang ul').addClass('secondary').before('<ul class="primary"></ul>');languages=['en','fr','de','es','pt','it','ru','ja','nl','pl','zh','sv','ar','tr','uk','fi','no','ca','ro','hu','ksh','id','he','cs','vi','ko','sr','fa','da','eo','sk','th','lt','vo','bg','sl','hr','hi','et','mk','simple','new','ms','nn','gl','el','eu','ka','tl','bn','lv','ml','bs','te','la','az','sh','war','br','is','mr','be-x-old','sq','cy','lb','ta','zh-classical','an','jv','ht','oc','bpy','ceb','ur','zh-yue','pms','scn','be','roa-rup','qu','af','sw','nds','fy','lmo','wa','ku','hy','su','yi','io','os','ga','ast','nap','vec','gu','cv','bat-smg','kn','uz','zh-min-nan','si','als','yo','li','gan','arz','sah','tt','bar','gd','tg','kk','pam','hsb','roa-tara','nah','mn','vls','gv','mi','am','ia','co','ne','fo','nds-nl','glk','mt','ang','wuu','dv','km','sco','bcl','mg','my','diq','tk','szl','ug','fiu-vro','sc','rm','nrm','ps','nv','hif','bo','se','sa','pnb','map-bms','lad','lij','crh',
'fur','kw','to','pa','jbo','ba','ilo','csb','wo','xal','krc','ckb','pag','ln','frp','mzn','ce','nov','kv','eml','gn','ky','pdc','lo','haw','mhr','dsb','stq','tpi','arc','hak','ie','so','bh','ext','mwl','sd','ig','myv','ay','iu','na','cu','pi','kl','ty','lbe','ab','got','sm','as','mo','ee','zea','av','ace','kg','bm','cdo','cbk-zam','kab','om','chr','pap','udm','ks','zu','rmy','cr','ch','st','ik','mdf','kaa','aa','fj','srn','tet','or','pnt','bug','ss','ts','pcd','pih','za','sg','lg','bxr','xh','ak','ha','bi','ve','tn','ff','dz','ti','ki','ny','rw','chy','tw','sn','tum','ng','rn','mh','ii','cho','hz','kr','ho','mus','kj'];acceptLangCookie=$.cookie('accept-language');if(acceptLangCookie!==null){if(acceptLangCookie!==''){languages=acceptLangCookie.split(',').concat(languages);}}else{$.getJSON(mw.util.wikiScript('api'),'format=json&action=query&meta=userinfo&uiprop=acceptlang',function(data){var langs=[],j,len,lang;if(data.query&&data.query.userinfo&&data.query.userinfo.acceptlang!==
undefined){for(j=0,lang=data.query.userinfo.acceptlang,len=lang.length;j<len;j++){if(lang[j].q!==0){langs.push(lang[j]['*']);}}}$.cookie('accept-language',langs.join(','),{path:'/',expires:30});});}$primary=$('#p-lang ul.primary');$secondary=$('#p-lang ul.secondary');if($secondary.children().length<limit+threshold){limit+=threshold;}count=0;for(i=0;i<languages.length;i++){$link=$secondary.find('.interwiki-'+languages[i]);if($link.length){if(count++<limit){$link.appendTo($primary);}else{break;}}}if(count<limit){$secondary.children().each(function(){if(count++<limit){$(this).appendTo($primary);}else{return false;}});}if($secondary.children().length===0){$secondary.remove();}else{$('#p-lang').after('<div id="p-lang-more" class="portal"><h3></h3><div class="body"></div></div>');$('#p-lang-more h3').text(mw.msg('vector-collapsiblenav-more'));$secondary.appendTo($('#p-lang-more .body'));}$('#p-lang').addClass('persistent');}$('#mw-panel > .portal:first').addClass('first persistent');$(
'#mw-panel').addClass('collapsible-nav');$('#mw-panel > .portal:not(.persistent)').each(function(i){var id=$(this).attr('id'),state=$.cookie('vector-nav-'+id);$(this).find('h3, h5').wrapInner($('<a href="#"></a>').click(false));if(state==='true'||(state===null&&i<1)||(state===null&&version===1&&id==='p-lang')){$(this).addClass('expanded').removeClass('collapsed').find('.body').hide().show();}else{$(this).addClass('collapsed').removeClass('expanded');}if(state!==null){$.cookie('vector-nav-'+$(this).attr('id'),state,{'expires':30,'path':'/'});}});$headings=$('#mw-panel > .portal:not(.persistent) > h3, #mw-panel > .portal:not(.persistent) > h5');tabIndex=$(document).lastTabIndex()+1;$('#searchInput').attr('tabindex',tabIndex++);$headings.attr('tabindex',function(){return tabIndex++;});$('#mw-panel').delegate('.portal:not(.persistent) > h3, .portal:not(.persistent) > h5','keydown',function(e){if(e.which===13||e.which===32){toggle($(this));}}).delegate(
'.portal:not(.persistent) > h3, .portal:not(.persistent) > h5','mousedown',function(e){if(e.which!==3){toggle($(this));$(this).blur();}return false;});});}(mediaWiki,jQuery));;},{"css":[
"#mw-panel.collapsible-nav .portal{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIwAAAABCAMAAAA7MLYKAAAAS1BMVEXb29vy8vLv7+/c3NzZ2dni4uLr6+vt7e3s7Ozw8PDn5+fj4+Ph4eHd3d3f39/o6Ojl5eXp6enx8fHa2trg4ODq6urk5OTz8/PY2NjolWftAAAAO0lEQVR4XrXAhwGAMAgEQB5I71X3n9QpPHqAGZidt2e02G8yedciQkv1/YPqIpFSdzbp9tjGsd4xhwl8yuMKHhkJhm8AAAAASUVORK5CYII=) left top no-repeat;background:url(//bits.wikimedia.org/static-1.22wmf3/extensions/Vector/modules/images/portal-break.png?2013-04-29T16:13:20Z) left top no-repeat!ie;padding:0.25em 0 !important;margin:-11px 9px 10px 11px}#mw-panel.collapsible-nav .portal h3,#mw-panel.collapsible-nav .portal h5{color:#4D4D4D;font-weight:normal;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAD1BMVEX////d3d2ampqxsbF5eXmCtCYvAAAAAXRSTlMAQObYZgAAADBJREFUeF6dzNEJACAMA1HdINQJCp1Ebv+ZlLYLaD4f4cbnDNi6MAO8KCHJ+7X02j3mzgMQe93HcQAAAABJRU5ErkJggg==) left center no-repeat;background:url(//bits.wikimedia.org/static-1.22wmf3/extensions/Vector/modules/images/open.png?2013-04-29T16:13:20Z) left center no-repeat!ie;padding:4px 0 3px 1.5em;margin-bottom:0}#mw-panel.collapsible-nav .portal h3:hover,#mw-panel.collapsible-nav .portal h5:hover{cursor:pointer;text-decoration:none}#mw-panel.collapsible-nav .portal h3 a,#mw-panel.collapsible-nav .portal h5 a{color:#4D4D4D;text-decoration:none}#mw-panel.collapsible-nav .portal .body{background:none !important;padding-top:0;display:none}#mw-panel.collapsible-nav .portal .body ul li{padding:0.25em 0} #mw-panel.collapsible-nav .portal.first h3,#mw-panel.collapsible-nav .portal.first h5{display:none}#mw-panel.collapsible-nav .portal.first{background-image:none;margin-top:0} #mw-panel.collapsible-nav .portal.persistent .body{display:block}#mw-panel.collapsible-nav .portal.persistent h3,#mw-panel.collapsible-nav .portal.persistent h5{background:none !important;padding-left:0.7em;cursor:default}#mw-panel.collapsible-nav .portal.persistent .body{margin-left:0.5em} #mw-panel.collapsible-nav .portal.collapsed h3,#mw-panel.collapsible-nav .portal.collapsed h5{color:#0645AD;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAADFBMVEX///95eXnd3d2dnZ3aAo3QAAAAAXRSTlMAQObYZgAAADFJREFUeF5dyzEKACAMA0CXolNe2Id09Kl5igZahWY4AiGjZwmIuS9GEcJfY63Ix88Bol4EYP1O7JMAAAAASUVORK5CYII=) left center no-repeat;background:url(//bits.wikimedia.org/static-1.22wmf3/extensions/Vector/modules/images/closed-ltr.png?2013-04-29T16:13:20Z) left center no-repeat!ie;margin-bottom:0}#mw-panel.collapsible-nav .portal.collapsed h3 a,#mw-panel.collapsible-nav .portal.collapsed h5 a{color:#0645AD}#mw-panel.collapsible-nav .portal.collapsed h3:hover,#mw-panel.collapsible-nav .portal.collapsed h5:hover{text-decoration:underline}\n/* cache key: enwiki:resourceloader:filter:minify-css:7:56c2944b859c6a975e16a79bea02c979 */"
]},{"vector-collapsiblenav-more":"More languages"});mw.loader.implement("ext.vector.collapsibleTabs",function(){jQuery(function($){var $cactions=$('#p-cactions');$('#p-views ul').bind('beforeTabCollapse',function(){if($cactions.hasClass('emptyPortlet')){$cactions.removeClass('emptyPortlet').find('h3, h5').css('width','1px').animate({'width':'24px'},390);}}).bind('beforeTabExpand',function(){if($cactions.find('li').length===1){$cactions.find('h3, h5').animate({'width':'1px'},390,function(){$(this).attr('style','').parent().addClass('emptyPortlet');});}}).collapsibleTabs();});;},{},{});mw.loader.implement("jquery.collapsibleTabs",function(){(function($){var rtl=$('body').is('.rtl');$.fn.collapsibleTabs=function(options){if(!this.length){return this;}var $settings=$.extend({},$.collapsibleTabs.defaults,options);this.each(function(){var $el=$(this);$.collapsibleTabs.instances=($.collapsibleTabs.instances.length===0?$el:$.collapsibleTabs.instances.add($el));$el.data(
'collapsibleTabsSettings',$settings);$el.children($settings.collapsible).each(function(){$.collapsibleTabs.addData($(this));});});if(!$.collapsibleTabs.boundEvent){$(window).delayedBind('500','resize',function(){$.collapsibleTabs.handleResize();});}$.collapsibleTabs.handleResize();return this;};function calculateTabDistance(){var $tabsArray,$leftTab,$rightTab,leftEnd,rightStart;if(!rtl){$leftTab=$('#left-navigation');$rightTab=$('#right-navigation');}else{$leftTab=$('#right-navigation');$rightTab=$('#left-navigation');}leftEnd=$leftTab.offset().left+$leftTab.width();rightStart=$rightTab.offset().left;return rightStart-leftEnd;}$.collapsibleTabs={instances:[],boundEvent:null,defaults:{expandedContainer:'#p-views ul',collapsedContainer:'#p-cactions ul',collapsible:'li.collapsible',shifting:false,expandCondition:function(eleWidth){return calculateTabDistance()>=eleWidth;},collapseCondition:function(){return calculateTabDistance()<0;}},addData:function($collapsible){var $settings=
$collapsible.parent().data('collapsibleTabsSettings');if($settings!==null){$collapsible.data('collapsibleTabsSettings',{expandedContainer:$settings.expandedContainer,collapsedContainer:$settings.collapsedContainer,expandedWidth:$collapsible.width(),prevElement:$collapsible.prev()});}},getSettings:function($collapsible){var $settings=$collapsible.data('collapsibleTabsSettings');if($settings===undefined){$.collapsibleTabs.addData($collapsible);$settings=$collapsible.data('collapsibleTabsSettings');}return $settings;},handleResize:function(){$.collapsibleTabs.instances.each(function(){var $el=$(this),data=$.collapsibleTabs.getSettings($el);if(data.shifting){return;}if($el.children(data.collapsible).length>0&&data.collapseCondition()){$el.trigger('beforeTabCollapse');$.collapsibleTabs.moveToCollapsed($el.children(data.collapsible+':last'));}if($(data.collapsedContainer+' '+data.collapsible).length>0&&data.expandCondition($.collapsibleTabs.getSettings($(data.collapsedContainer).children(
data.collapsible+':first')).expandedWidth)){$el.trigger('beforeTabExpand');$.collapsibleTabs.moveToExpanded(data.collapsedContainer+' '+data.collapsible+':first');}});},moveToCollapsed:function(ele){var $moving=$(ele);var data=$.collapsibleTabs.getSettings($moving);if(!data){return;}var expContainerSettings=$.collapsibleTabs.getSettings($(data.expandedContainer));if(!expContainerSettings){return;}expContainerSettings.shifting=true;var target=data.collapsedContainer;$moving.css('position','relative').css((rtl?'left':'right'),0).animate({width:'1px'},'normal',function(){var data;$(this).hide();$('<span class="placeholder" style="display: none;"></span>').insertAfter(this);$(this).detach().prependTo(target).data('collapsibleTabsSettings',data);$(this).attr('style','display: list-item;');data=$.collapsibleTabs.getSettings($(ele));if(data){var expContainerSettings=$.collapsibleTabs.getSettings($(data.expandedContainer));if(expContainerSettings){expContainerSettings.shifting=false;$.
collapsibleTabs.handleResize();}}});},moveToExpanded:function(ele){var $moving=$(ele);var data=$.collapsibleTabs.getSettings($moving);if(!data){return;}var expContainerSettings=$.collapsibleTabs.getSettings($(data.expandedContainer));if(!expContainerSettings){return;}expContainerSettings.shifting=true;var $target=$(data.expandedContainer).find('span.placeholder:first');var expandedWidth=data.expandedWidth;$moving.css('position','relative').css((rtl?'right':'left'),0).css('width','1px');$target.replaceWith($moving.detach().css('width','1px').data('collapsibleTabsSettings',data).animate({width:expandedWidth+'px'},'normal',function(){$(this).attr('style','display: block;');var data=$.collapsibleTabs.getSettings($(this));if(data){var expContainerSettings=$.collapsibleTabs.getSettings($(data.expandedContainer));if(expContainerSettings){expContainerSettings.shifting=false;$.collapsibleTabs.handleResize();}}}));}};}(jQuery));;},{},{});
/* cache key: enwiki:resourceloader:filter:minify-js:7:62c595a3dff032ffad53e1bed4d4e6f1 */