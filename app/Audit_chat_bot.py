import streamlit as st
import streamlit.components.v1 as components


html_code = f"""
<div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
    <h1 style="margin: 0 15px 0 0;">Horizon&apos;s Edge AI</h1>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)

body = """
<div dir="rtl">
  <div id="vf-chat" style="width: 100%; height: 600px; border-radius: 20px; overflow: hidden;"></div>

  <script type="text/javascript">
    (function(d, t) {
        var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
        v.onload = function() {
          window.voiceflow.chat.load({
            verify: { projectID: '67cab1ea1959363ad652ea5a' },
            url: 'https://general-runtime.voiceflow.com',
            versionID: 'production',
            voice: {
              url: "https://runtime-api.voiceflow.com"
            },
            render: {
              mode: 'embedded',
              target: document.getElementById('vf-chat')
            },
            customStyle: {
              css: `
                .vfrc-chat {
                  border-radius: 20px !important;
                  direction: rtl;
                  text-align: right;
                }
              `
            }
          });
        };
        v.src = "https://cdn.voiceflow.com/widget-next/bundle.mjs";
        v.type = "text/javascript";
        s.parentNode.insertBefore(v, s);
    })(document, 'script');
  </script>
</div>
"""

components.html(body, height=620)
