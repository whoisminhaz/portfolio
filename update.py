import re
import sys

def process():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()
        
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # 1. Update hero stats in HTML
    new_hero_stats = """                <div class="hero-stats">
                    <div class="stat"><span class="stat-num" data-count="4">0</span><span class="stat-label">Languages Spoken</span><span class="stat-desc">English (C1/IELTS 7.5), Bangla, Hindi, Urdu</span></div>
                    <div class="stat"><span class="stat-num" data-count="7.5" data-decimal="true">0</span><span class="stat-label">IELTS Band</span><span class="stat-desc">Advanced Professional Proficiency</span></div>
                    <div class="stat"><span class="stat-num" data-count="5">0</span><span class="stat-label">Merit Scholarships</span><span class="stat-desc">3 International, 2 National</span></div>
                    <div class="stat"><div class="stat-num-wrapper"><span class="stat-num" data-count="4">0</span><span class="stat-plus">+</span></div><span class="stat-label">Active Ventures</span><span class="stat-desc">Including BAJOWS News & DOT ZERO</span></div>
                </div>"""
    html = re.sub(r'<div class="hero-stats">.*?</div>\s*</div>\s*<div class="hero-cta">', new_hero_stats + '\n                <div class="hero-cta">', html, flags=re.DOTALL)

    # 2. Update CSS for hero stats
    new_css_stats = """.hero-stats{display:flex;gap:32px;margin-bottom:32px}
.stat{display:flex;flex-direction:column;align-items:center;text-align:center}
.stat-num-wrapper{display:flex;align-items:baseline;justify-content:center}
.stat-num{font-family:var(--display);font-size:38px;font-weight:700;display:block;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1}
.stat-plus{font-family:var(--display);font-size:24px;font-weight:700;color:var(--accent);margin-left:2px}
.stat-label{font-size:13px;font-weight:600;color:var(--text);margin:6px 0 4px}
.stat-desc{font-size:11px;color:var(--text2);max-width:140px;line-height:1.4}"""
    css = re.sub(r'\.hero-stats\{.*?\.stat-label\{.*?\}', new_css_stats, css, flags=re.DOTALL)

    # 3. Add glow-card and cursor-glow to CSS
    glow_css = """
/* CURSOR & GLOW EFFECTS */
#cursor-glow{position:fixed;top:0;left:0;width:600px;height:600px;background:radial-gradient(circle,rgba(108,92,231,0.06) 0%,transparent 70%);border-radius:50%;pointer-events:none;transform:translate(-50%,-50%);z-index:9999;transition:opacity 0.3s}
.glow-card{position:relative;background:var(--card);border-radius:var(--r);transition:all var(--t);border:1px solid var(--border)}
.glow-card::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;background:radial-gradient(400px circle at var(--mouse-x, -200px) var(--mouse-y, -200px), var(--glow-color, rgba(108,92,231,0.6)), transparent 40%);-webkit-mask:linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;z-index:10;transition:opacity 0.3s;opacity:0}
.glow-container:hover .glow-card::before{opacity:1}
.glow-btn{padding:8px 16px;border-radius:100px;font-size:12px;font-weight:600;color:#fff;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);transition:all 0.3s;text-decoration:none;display:inline-block}
.glow-btn:hover{border-color:var(--btn-color);box-shadow:0 0 15px var(--btn-color);background:rgba(255,255,255,0.1)}
"""
    css = css.replace("/* BUTTONS */", glow_css + "/* BUTTONS */")

    # 4. JS for glow
    js_glow = """
// CURSOR & GLOW
const cursorGlow = document.createElement('div');
cursorGlow.id = 'cursor-glow';
document.body.appendChild(cursorGlow);
window.addEventListener('mousemove', e => {
    cursorGlow.style.left = e.clientX + 'px';
    cursorGlow.style.top = e.clientY + 'px';
});
document.querySelectorAll('.glow-container').forEach(container => {
    container.addEventListener('mousemove', e => {
        container.querySelectorAll('.glow-card').forEach(card => {
            const rect = card.getBoundingClientRect();
            card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
            card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
        });
    });
});
"""
    js += js_glow

    # 5. Fix Skills Grid to use tags and glow-cards
    new_skills_css = """
.skills-tri{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.skill-block{position:relative;padding:28px;border-radius:var(--r);overflow:hidden;transition:all var(--t)}
.skill-block:hover{transform:translateY(-4px);box-shadow:0 10px 30px rgba(0,0,0,0.2)}
.skill-block h3{font-size:16px;font-weight:700;margin-bottom:20px;display:flex;align-items:center;gap:10px}
.skill-tags{display:flex;flex-wrap:wrap;gap:10px}
.skill-tag{padding:6px 14px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);border-radius:100px;font-size:12px;color:var(--text2);transition:var(--t);cursor:default}
.skill-tag:hover{background:var(--card-h);border-color:var(--accent);color:#fff;box-shadow:0 0 12px rgba(108,92,231,0.2)}
"""
    css = re.sub(r'\.skills-tri\{.*?\.skill-block li\{.*?\}', new_skills_css, css, flags=re.DOTALL)

    new_skills_html = """            <div class="skills-tri glow-container reveal">
                <div class="glow-card skill-block" data-tilt style="--glow-color: #6c5ce7;">
                    <h3>🗣️ Soft Skills</h3>
                    <div class="skill-tags"><span class="skill-tag">Public Speaking</span><span class="skill-tag">Persuasion & Negotiation</span><span class="skill-tag">Understanding People</span><span class="skill-tag">Active Listening</span><span class="skill-tag">Strategic Thinking</span><span class="skill-tag">Problem-Solving</span><span class="skill-tag">Team Leadership</span><span class="skill-tag">Adaptability</span><span class="skill-tag">Communication</span></div>
                </div>
                <div class="glow-card skill-block" data-tilt style="--glow-color: #00cec9;">
                    <h3>📊 Hard Skills</h3>
                    <div class="skill-tags"><span class="skill-tag">Data Analysis</span><span class="skill-tag">E-Commerce & Sales</span><span class="skill-tag">Social Media Management</span><span class="skill-tag">Content Strategy</span><span class="skill-tag">AI Marketing & Automation</span><span class="skill-tag">Business Development</span><span class="skill-tag">Project Management</span><span class="skill-tag">Event Management</span><span class="skill-tag">Video Editing</span></div>
                </div>
                <div class="glow-card skill-block" data-tilt style="--glow-color: #e84393;">
                    <h3>⚡ Tech & Tools</h3>
                    <div class="skill-tags"><span class="skill-tag">Microsoft Office Suite</span><span class="skill-tag">Notion</span><span class="skill-tag">Google AI Studio</span><span class="skill-tag">Antigravity AI</span><span class="skill-tag">NotebookLLM</span><span class="skill-tag">ICT Fundamentals</span><span class="skill-tag">Video Production Tools</span><span class="skill-tag">Social Media Platforms</span><span class="skill-tag">AI Automation Tools</span></div>
                </div>
            </div>"""
    html = re.sub(r'<div class="skills-tri reveal">.*?</div>\s*</div>\s*</section>', new_skills_html + '\n        </div>\n    </section>', html, flags=re.DOTALL)

    # 6. Venture Links glow
    html = html.replace('<a href="https://whoisminhaz.github.io/dotzero/" target="_blank" class="btn btn-outline btn-sm">Project Site</a>', '<a href="https://whoisminhaz.github.io/dotzero/" target="_blank" class="glow-btn" style="--btn-color: #00cec9;">Project Site</a>')
    html = html.replace('<a href="https://dotzero.whoisminhaz.workers.dev/" target="_blank" class="btn btn-outline btn-sm">Mirror</a>', '<a href="https://dotzero.whoisminhaz.workers.dev/" target="_blank" class="glow-btn" style="--btn-color: #6c5ce7;">Mirror</a>')

    # 7. Add References before Contact
    ref_html = """
    <!-- REFERENCES -->
    <section id="references">
        <div class="container">
            <div class="section-header reveal"><span class="section-tag">07 — References</span><h2 class="section-title">Professional<br><span class="accent">Endorsements.</span></h2></div>
            <div class="ref-grid glow-container">
                <div class="ref-card glow-card reveal" style="--glow-color: #00cec9;">
                    <div class="ref-quote">"Minhaz has consistently shown an exceptional ability to lead and execute projects with a level of strategic thinking far beyond his years."</div>
                    <div class="ref-author">
                        <div class="ref-avatar">A</div>
                        <div class="ref-info">
                            <strong>Prof. Albukhary</strong>
                            <span>Academic Director</span>
                        </div>
                    </div>
                </div>
                <div class="ref-card glow-card reveal" style="--glow-color: #6c5ce7;">
                    <div class="ref-quote">"His capability to quickly synthesize data and translate it into actionable business strategy was instrumental during the national competition."</div>
                    <div class="ref-author">
                        <div class="ref-avatar">S</div>
                        <div class="ref-info">
                            <strong>Dr. Syed Saad Andaleeb</strong>
                            <span>Former Vice-Chancellor, BRAC University</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
    html = html.replace('<!-- CONTACT -->', ref_html + '\n    <!-- CONTACT -->')
    html = html.replace('07 — Contact', '08 — Contact')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    
    print("Done")

if __name__ == "__main__":
    process()
