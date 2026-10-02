// Public PostHog project token. Never place a personal API key here.
(() => {
  if (location.protocol !== 'https:' || !['vibegraph.md', 'www.vibegraph.md'].includes(location.hostname) || window.posthog) return;

  !function(t,e){var o,n,p,r;e.__SV||(window.posthog && window.posthog.__loaded)||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}p||((p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",p.onerror=function(){p=null},(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r));var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],Object.defineProperty(u,"toString",{configurable:!0,enumerable:!0,writable:!0,value:function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e}}),Object.defineProperty(u.people,"toString",{configurable:!0,enumerable:!0,writable:!0,value:function(){return u.toString(1)+".people (stub)"}}),o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagResult isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
  window.posthog.init('phc_kVJ2cQPG47sz6gohqzmCvDYF6hWj4SWP3AtNpviWwPST', {
    api_host: 'https://us.i.posthog.com',
    defaults: '2026-05-30',
    capture_pageview: true,
    capture_pageleave: true,
    person_profiles: 'identified_only',
    autocapture: false,
    capture_dead_clicks: false,
    disable_session_recording: true,
    enable_recording_console_log: false,
    loaded: (posthog) => posthog.register({ site_domain: location.hostname.replace(/^www\./, '') }),
  });

  document.addEventListener('click', (event) => {
    const link = event.target?.closest?.('a[href]');
    if (!link) return;
    let url;
    try { url = new URL(link.href, location.href); } catch { return; }
    if (!['https:', 'http:'].includes(url.protocol)) return;
    const download = link.hasAttribute('download') || /\.(pdf|zip)$/i.test(url.pathname);
    if (!download && url.hostname === location.hostname) return;
    window.posthog.capture(download ? 'file_download_clicked' : 'outbound_link_clicked', {
      destination_host: url.hostname,
      destination_path: url.pathname,
      site_domain: location.hostname.replace(/^www\./, ''),
    });
  });
})();
