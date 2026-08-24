/**
 * THE HOUSE — SENSORY INMERSIVE SHADER & SCROLL ENGINE (MÓDULO 26 & 27)
 * Armenia, Quindío · Three.js GLSL Shader + Lenis 1.x + GSAP ScrollTrigger
 */

const HOUSE_STATE = {
    stage: 1, // 1: 30%, 2: 40%, 3: 50%, 4: 60%, 5: 70%
    stagePercentages: {
        1: { pct: 30, label: 'Mes 1-2 · Inducción (30% Modelo / 70% Estudio)' },
        2: { pct: 40, label: 'Mes 3-4 · Despegue (40% Modelo / 60% Estudio)' },
        3: { pct: 50, label: 'Mes 5-6 · Consolidación (50% Modelo / 50% Estudio)' },
        4: { pct: 60, label: 'Mes 7-8 · Avanzado (60% Modelo / 40% Estudio)' },
        5: { pct: 70, label: 'Mes 9+ · Élite (70% Modelo / 30% Estudio)' }
    },
    trm: 4100.0,
    leads: [],
    sessionMemory: {
        lastExploredTalent: null,
        interactionScore: 0,
        favoredMood: 'velvet'
    }
};

// Shaders GLSL para Fondo Respiratorio
const VERTEX_SHADER = `
varying vec2 vUv;
void main() {
    vUv = uv;
    gl_Position = vec4(position, 1.0);
}
`;

const FRAGMENT_SHADER = `
uniform float uTime;
uniform vec2 uResolution;
uniform vec2 uCursor;
uniform float uActBreathingFreq;
uniform float uTensionLevel;
uniform vec3 uColorBase;
uniform vec3 uColorAccent;

varying vec2 vUv;

// Simplex Noise Generator 2D
vec3 permute(vec3 x) { return mod(((x*34.0)+1.0)*x, 289.0); }
float snoise(vec2 v){
   const vec4 C = vec4(0.211324865405187, 0.366025403784439,
                      -0.577350269189626, 0.024390243902439);
   vec2 i  = floor(v + dot(v, C.yy) );
   vec2 x0 = v -   i + dot(i, C.xx);
   vec2 i1;
   i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
   vec4 x12 = x0.xyxy + C.xxzz;
   x12.xy -= i1;
   i  = mod(i, 289.0);
   vec3 p = permute( permute( i.y + vec3(0.0, i1.y, 1.0 ))
   + i.x + vec3(0.0, i1.x, 1.0 ) );
   vec3 m = max(0.5 - vec3(dot(x0,x0), dot(x12.xy,x12.xy), dot(x12.zw,x12.zw)), 0.0);
   m = m*m ;
   m = m*m ;
   vec3 x = 2.0 * fract(p * C.www) - 1.0;
   vec3 h = abs(x) - 0.5;
   vec3 ox = floor(x + 0.5);
   vec3 a0 = x - ox;
   m *= 1.79284291400159 - 0.85373472095314 * ( a0*a0 + h*h );
   vec3 g;
   g.x  = a0.x  * x0.x  + h.x  * x0.y;
   g.yz = a0.yz * x12.xz + h.yz * x12.yw;
   return 130.0 * dot(m, g);
}

void main() {
   vec2 st = gl_FragCoord.xy / uResolution.xy;
   vec2 cursorNorm = uCursor / uResolution;
   
   // Breathing frequency calculation ultra-slow
   float breath = sin(uTime * uActBreathingFreq) * 0.5 + 0.5;
   
   // Distort UVs based on cursor proximity and tension
   vec2 distUv = st + (cursorNorm - st) * (0.02 * uTensionLevel);
   float noiseVal = snoise(distUv * 2.0 + vec2(uTime * 0.03));
   
   // Combine base breathing and micro-texture
   float finalMask = smoothstep(0.1, 0.9, noiseVal + (breath * 0.22));
   vec3 finalColor = mix(uColorBase, uColorAccent, finalMask * 0.14);
   
   // Vignette implementation
   float vignette = length(st - vec2(0.5));
   finalColor *= smoothstep(0.85, 0.25, vignette * 1.15);

   gl_FragColor = vec4(finalColor, 1.0);
}
`;

document.addEventListener('DOMContentLoaded', () => {
    initSensoryCursor();
    initMagneticElements();
    initNavbarActiveState();
    initWebGLBackground();
    initLenisAndScrollTrigger();
    initBreathingParallax();
    initKeyboardShortcuts();
    initSessionMemory();
    fetchTrmRate();
    updateOpportunityCalc();
    initAgeGate();
    initScrollPopVideos();
    initFixedWatermarkVisibility();
    initFloatingSocialHub();
});

// ==========================================================================
// 1. LIENZO WEBGL GLSL: SHADER DE FONDO RESPIRATORIO (THREE.JS)
// ==========================================================================
let shaderUniforms;
function initWebGLBackground() {
    const canvas = document.getElementById('webglCanvas');
    if (!canvas || typeof THREE === 'undefined') return;

    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: "high-performance" });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const scene = new THREE.Scene();
    const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);

    shaderUniforms = {
        uTime: { value: 0 },
        uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
        uCursor: { value: new THREE.Vector2(window.innerWidth / 2, window.innerHeight / 2) },
        uActBreathingFreq: { value: 0.035 }, // Respiración inicial ultra-lenta
        uTensionLevel: { value: 0.2 },
        uColorBase: { value: new THREE.Color(0x080807) },
        uColorAccent: { value: new THREE.Color(0xB7A17A) }
    };

    const material = new THREE.ShaderMaterial({
        vertexShader: VERTEX_SHADER,
        fragmentShader: FRAGMENT_SHADER,
        uniforms: shaderUniforms,
        transparent: true
    });

    const plane = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
    scene.add(plane);

    window.addEventListener('resize', () => {
        renderer.setSize(window.innerWidth, window.innerHeight);
        shaderUniforms.uResolution.value.set(window.innerWidth, window.innerHeight);
    });

    window.addEventListener('mousemove', (e) => {
        shaderUniforms.uCursor.value.set(e.clientX, window.innerHeight - e.clientY);
    });

    function render(time) {
        shaderUniforms.uTime.value = time * 0.001;
        renderer.render(scene, camera);
        requestAnimationFrame(render);
    }
    requestAnimationFrame(render);
}

// ==========================================================================
// 2. MICRO-PARALLAX RESPIRATORIO
// ==========================================================================
function initBreathingParallax() {
    let targetX = 0, targetY = 0;
    let currentX = 0, currentY = 0;

    window.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 2;
        const y = (e.clientY / window.innerHeight - 0.5) * 2;
        targetX = x * 6;
        targetY = y * 5;
    });

    function updateParallax() {
        currentX += (targetX - currentX) * 0.05;
        currentY += (targetY - currentY) * 0.05;

        document.documentElement.style.setProperty('--parallax-bg-x', `${currentX * 0.6}px`);
        document.documentElement.style.setProperty('--parallax-bg-y', `${currentY * 0.6}px`);
        document.documentElement.style.setProperty('--parallax-light-x', `${-currentX * 1.2}px`);
        document.documentElement.style.setProperty('--parallax-light-y', `${-currentY * 1.2}px`);

        requestAnimationFrame(updateParallax);
    }
    updateParallax();
}

// ==========================================================================
// 3. SCROLL CINEMÁTICO: LENIS 1.X + GSAP SCROLLTRIGGER (UNIFIED TICKER)
// ==========================================================================
function initLenisAndScrollTrigger() {
    if (typeof Lenis === 'undefined' || typeof gsap === 'undefined') {
        initFallbackScroll();
        return;
    }

    gsap.registerPlugin(ScrollTrigger);

    const lenis = new Lenis({
        lerp: 0.07,          // Inercia aristocrática
        syncTouch: true,
        wheelMultiplier: 0.88
    });

    lenis.on('scroll', ScrollTrigger.update);

    // Unificar loop RAF vía GSAP Ticker con lagSmoothing(0)
    gsap.ticker.add((time) => {
        lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);

    // Scroll Pacing & Modulación de Shaders por Acto
    const acts = [
        { id: '#actArrival', freq: 0.035, tension: 0.2 },
        { id: '#manifesto', freq: 0.06, tension: 0.3 },
        { id: '#the-house', freq: 0.10, tension: 0.5 },
        { id: '#the-talent', freq: 0.18, tension: 0.7 },
        { id: '#the-craft', freq: 0.14, tension: 0.6 },
        { id: '#the-experience', freq: 0.12, tension: 0.4 },
        { id: '#privacy', freq: 0.05, tension: 0.3 },
        { id: '#opportunity', freq: 0.12, tension: 0.5 },
        { id: '#application', freq: 0.05, tension: 0.15 }
    ];

    acts.forEach(act => {
        const el = document.querySelector(act.id);
        if (!el) return;

        ScrollTrigger.create({
            trigger: el,
            start: "top center",
            end: "bottom center",
            onEnter: () => updateShaderAct(act.freq, act.tension),
            onEnterBack: () => updateShaderAct(act.freq, act.tension)
        });
    });

    // Scroll Reveals Generales
    document.querySelectorAll('.scroll-reveal, .image-mask-reveal').forEach(el => {
        ScrollTrigger.create({
            trigger: el,
            start: "top 85%",
            onEnter: () => el.classList.add('revealed')
        });
    });

    // Stagger Ultra Suave para Tarjetas de Estrategia Sonora y Video Reels
    if (typeof ScrollTrigger.batch === 'function') {
        ScrollTrigger.batch(".music-moods-grid .music-card, .video-reels-grid .video-reel-card", {
            start: "top 88%",
            onEnter: (batch) => {
                batch.forEach((card, i) => {
                    setTimeout(() => {
                        card.classList.add('revealed');
                    }, i * 140);
                });
            },
            once: true
        });
    }
}

function updateShaderAct(freq, tension) {
    if (!shaderUniforms) return;
    gsap.to(shaderUniforms.uActBreathingFreq, { value: freq, duration: 2.0, ease: "power2.out" });
    gsap.to(shaderUniforms.uTensionLevel, { value: tension, duration: 2.0, ease: "power2.out" });
}

function initFallbackScroll() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('revealed'); });
    }, { threshold: 0.15 });

    document.querySelectorAll('.scroll-reveal, .image-mask-reveal').forEach(el => observer.observe(el));
}

// ==========================================================================
// 4. CURSOR SENSORIAL (DESTELLO SUAVE) & ESTADO ACTIVO NAVBAR
// ==========================================================================
function initSensoryCursor() {
    const dot = document.getElementById('sensoryCursorDot');
    const halo = document.getElementById('sensoryCursorHalo');
    if (!dot || !halo) return;

    window.addEventListener('mousemove', (e) => {
        dot.style.left = `${e.clientX}px`;
        dot.style.top = `${e.clientY}px`;
        
        halo.style.left = `${e.clientX}px`;
        halo.style.top = `${e.clientY}px`;
    });

    document.querySelectorAll('a, button, input, select, textarea, .space-editorial-card, .talent-profile-card, .craft-card').forEach(el => {
        el.addEventListener('mouseenter', () => {
            halo.style.width = '88px';
            halo.style.height = '88px';
            halo.style.background = 'radial-gradient(circle, rgba(255, 230, 190, 0.35) 0%, rgba(200, 165, 110, 0.15) 50%, rgba(183, 161, 122, 0) 80%)';
            dot.style.width = '14px';
            dot.style.height = '14px';
            dot.style.boxShadow = '0 0 22px 6px rgba(255, 240, 215, 0.95), 0 0 40px 10px rgba(215, 180, 125, 0.6)';
        });
        el.addEventListener('mouseleave', () => {
            halo.style.width = '56px';
            halo.style.height = '56px';
            halo.style.background = 'radial-gradient(circle, rgba(240, 215, 175, 0.25) 0%, rgba(183, 161, 122, 0.1) 45%, transparent 75%)';
            dot.style.width = '10px';
            dot.style.height = '10px';
            dot.style.boxShadow = '0 0 16px 3px rgba(255, 235, 205, 0.85), 0 0 30px 6px rgba(183, 161, 122, 0.5)';
        });
    });
}

function initNavbarActiveState() {
    const navLinks = document.querySelectorAll('.nav-links-menu a');
    if (!navLinks.length) return;

    const trackedSections = [
        'manifesto',
        'the-craft',
        'the-experience',
        'privacy'
    ];

    function setActiveNav(targetId) {
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href === `#${targetId}` || href === `index.html#${targetId}`) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    // Click handler for instant blood-red glow feedback
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });

    // Scroll spy integration with GSAP ScrollTrigger
    if (typeof ScrollTrigger !== 'undefined') {
        trackedSections.forEach(id => {
            const section = document.getElementById(id);
            if (!section) return;

            ScrollTrigger.create({
                trigger: section,
                start: 'top 40%',
                end: 'bottom 40%',
                onEnter: () => setActiveNav(id),
                onEnterBack: () => setActiveNav(id)
            });
        });
    }
}

function initMagneticElements() {
    const magnetics = document.querySelectorAll('.magnetic-element');
    magnetics.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = (e.clientX - rect.left - rect.width / 2) * 0.18;
            const y = (e.clientY - rect.top - rect.height / 2) * 0.18;
            btn.style.transform = `translate(${x}px, ${y}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translate(0px, 0px)';
        });
    });
}

// ==========================================================================
// 5. MEMORIA VISUAL DE SESIÓN (SESSION VISUAL MEMORY)
// ==========================================================================
function initSessionMemory() {
    document.querySelectorAll('[data-talent]').forEach(card => {
        card.addEventListener('mouseenter', () => {
            const talent = card.getAttribute('data-talent');
            HOUSE_STATE.sessionMemory.lastExploredTalent = talent;
            HOUSE_STATE.sessionMemory.interactionScore += 1;
            
            if (shaderUniforms) {
                gsap.to(shaderUniforms.uColorAccent.value, { r: 0.76, g: 0.68, b: 0.52, duration: 2.5 });
            }
        });
    });
}

// ==========================================================================
// 6. CAMUFLAJE RÁPIDO & TECLA ESC
// ==========================================================================
function toggleCamouflage(show) {
    const camou = document.getElementById('camouflageScreen');
    if (show) {
        camou.style.display = 'block';
    } else {
        camou.style.display = 'none';
    }
}

function initKeyboardShortcuts() {
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const modal = document.getElementById('applicationModal');
            if (modal && modal.classList.contains('is-active')) {
                closeApplicationModal();
                return;
            }
            const camou = document.getElementById('camouflageScreen');
            if (camou) {
                const isShown = camou.style.display === 'block';
                toggleCamouflage(!isShown);
            }
        }
    });
}

// ==========================================================================
// 7. TRM EN TIEMPO REAL & CALCULADORA
// ==========================================================================
async function fetchTrmRate() {
    try {
        const res = await fetch('https://open.er-api.com/v6/latest/USD');
        if (res.ok) {
            const data = await res.json();
            if (data.rates && data.rates.COP) {
                HOUSE_STATE.trm = data.rates.COP;
                updateOpportunityCalc();
            }
        }
    } catch (e) {
        console.log('TRM contingencia: 4,100 COP');
    }
}

function setGrowthStage(stageNum) {
    HOUSE_STATE.stage = stageNum;
    for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`btnStage${i}`);
        if (btn) {
            if (i === stageNum) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        }
    }
    const stageInfo = HOUSE_STATE.stagePercentages[stageNum];
    const lbl = document.getElementById('lblModNombre');
    if (lbl && stageInfo) {
        lbl.textContent = stageInfo.label;
    }
    updateOpportunityCalc();
}

function updateOpportunityCalc() {
    const range = document.getElementById('rangeHoras');
    if (!range) return;

    const horas = parseInt(range.value, 10);
    const valHorasEl = document.getElementById('valHoras');
    if (valHorasEl) {
        valHorasEl.textContent = `${horas} hrs/sem`;
    }

    // Promedio de producción estimada en tokens por hora (125 tokens/hr = $6.25 USD/hr bruto)
    const tokensHora = 125.0;
    const gananciaBrutaSemanaUsd = horas * tokensHora * 0.05;

    const stageInfo = HOUSE_STATE.stagePercentages[HOUSE_STATE.stage] || { pct: 30 };
    const comision = stageInfo.pct; // 30%, 40%, 50%, 60%, 70%

    const netaSemanaUsd = gananciaBrutaSemanaUsd * (comision / 100.0);
    const netaMesUsd = netaSemanaUsd * 4.33;
    const netaMesCop = netaMesUsd * HOUSE_STATE.trm;

    const lblUsd = document.getElementById('lblUsdMonth');
    const lblCop = document.getElementById('lblCopMonth');
    if (lblUsd) {
        lblUsd.textContent = `$ ${netaMesUsd.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })} USD`;
    }
    if (lblCop) {
        lblCop.textContent = `≈ $ ${Math.round(netaMesCop).toLocaleString('es-CO')} COP`;
    }
}

// ==========================================================================
// 8. FORMULARIO DE POSTULACIÓN CONFIDENCIAL & RADICADO AXM
// ==========================================================================
async function handleHouseSubmit(event) {
    event.preventDefault();

    const nombre = document.getElementById('appNombre').value.trim();
    const whatsapp = document.getElementById('appWhatsapp').value.trim();
    const edad = parseInt(document.getElementById('appEdad').value, 10);
    const categoria = document.getElementById('appCategoria') ? document.getElementById('appCategoria').value : 'Mujer';
    const ciudad = document.getElementById('appCiudad').value;
    const experiencia = document.getElementById('appExperiencia') ? document.getElementById('appExperiencia').value : 'Sin Experiencia';
    const comentarios = document.getElementById('appComentarios').value.trim();
    const habeas = document.getElementById('appHabeas').checked;

    if (!habeas || !nombre || !whatsapp) return;

    const btn = document.getElementById('btnSubmitApp');
    if (btn) {
        btn.disabled = true;
        btn.textContent = 'PROCESANDO POSTULACIÓN CONFIDENCIAL...';
    }

    const radicadoId = `AXM-${Math.random().toString(36).substring(2, 8).toUpperCase()}`;
    const stageInfo = HOUSE_STATE.stagePercentages[HOUSE_STATE.stage] || { pct: 30 };
    const leadData = {
        radicado_id: radicadoId,
        timestamp: new Date().toISOString(),
        nombre: nombre,
        whatsapp: whatsapp,
        edad: edad,
        categoria: categoria,
        ciudad: ciudad,
        experiencia: experiencia,
        escala_seleccionada: `${stageInfo.pct}%`,
        comentarios: comentarios,
        habeas_data_autorizado: true,
        estado_gestion: 'POSTULACION_CONFIDENCIAL_RECIBIDA'
    };

    try {
        await fetch('/api/leads', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(leadData)
        });
    } catch (e) {
        console.log('Guardado local en base de datos...');
    }

    const cleanWa = "573001234567";
    const msg = encodeURIComponent(`Hola JD GROUP (Armenia), he enviado mi postulación confidencial con radicado: ${radicadoId} (Nombre/Alias: ${nombre}, Categoría: ${categoria}, Ciudad: ${ciudad}).`);
    const waUrl = `https://wa.me/${cleanWa}?text=${msg}`;

    setTimeout(() => {
        document.getElementById('houseApplicationForm').style.display = 'none';
        document.getElementById('appSuccessVoucher').style.display = 'block';
        document.getElementById('lblAppRadicado').textContent = radicadoId;
        document.getElementById('btnAppWa').href = waUrl;
    }, 600);
}

// ==========================================================================
// 9. CONTROLADOR DE REELS Y VIDEOS DE MENTORÍA
// ==========================================================================
function toggleReelPlay(btnElement) {
    const container = btnElement.closest('.video-reel-container');
    if (!container) return;
    const video = container.querySelector('.reel-video-element');
    if (!video) return;

    // Pausar cualquier otro video que esté reproduciéndose
    document.querySelectorAll('.reel-video-element').forEach(otherVideo => {
        if (otherVideo !== video && !otherVideo.paused) {
            otherVideo.pause();
            const otherBtn = otherVideo.closest('.video-reel-container')?.querySelector('.btn-reel-play');
            if (otherBtn) {
                otherBtn.classList.remove('is-playing');
                otherBtn.innerHTML = '<span class="play-icon">▶</span>';
            }
        }
    });

    if (video.paused) {
        video.play();
        btnElement.classList.add('is-playing');
        btnElement.innerHTML = '<span class="play-icon">❚❚</span>';
    } else {
        video.pause();
        btnElement.classList.remove('is-playing');
        btnElement.innerHTML = '<span class="play-icon">▶</span>';
    }
}

// ==========================================================================
// 10. SELECTOR INTERACTIVO DE SEDES (MOCAWA & GRANADA)
// ==========================================================================
function switchSedeView(sedeKey) {
    const tabMocawa = document.getElementById('tabSedeMocawa');
    const tabGranada = document.getElementById('tabSedeGranada');
    const panelMocawa = document.getElementById('sedeMocawaContent');
    const panelGranada = document.getElementById('sedeGranadaContent');

    if (!tabMocawa || !tabGranada || !panelMocawa || !panelGranada) return;

    if (sedeKey === 'mocawa') {
        tabMocawa.classList.add('active');
        tabGranada.classList.remove('active');

        panelMocawa.style.display = 'block';
        panelGranada.style.display = 'none';
        panelMocawa.classList.add('active');
        panelGranada.classList.remove('active');
    } else {
        tabGranada.classList.add('active');
        tabMocawa.classList.remove('active');

        panelGranada.style.display = 'block';
        panelMocawa.style.display = 'none';
        panelGranada.classList.add('active');
        panelMocawa.classList.remove('active');
    }

    // Refrescar GSAP ScrollTrigger para recalcular posiciones
    if (typeof ScrollTrigger !== 'undefined') {
        setTimeout(() => {
            ScrollTrigger.refresh();
        }, 100);
    }
}

// ==========================================================================
// 11. MODAL EMERGENTE DE POSTULACIÓN CONFIDENCIAL
// ==========================================================================
function openApplicationModal() {
    const modal = document.getElementById('applicationModal');
    if (modal) {
        modal.style.display = 'flex';
        setTimeout(() => {
            modal.classList.add('is-active');
            
            // Auto-play & pop video inside modal
            const modalReel = modal.querySelector('.video-reel-card');
            const modalVideo = modal.querySelector('.reel-video-element');
            const modalBtn = modal.querySelector('.btn-reel-play');
            if (modalReel) modalReel.classList.add('is-popped');
            if (modalVideo) {
                modalVideo.muted = true;
                modalVideo.play().then(() => {
                    if (modalBtn) modalBtn.classList.add('is-playing');
                }).catch(() => {});
            }
        }, 10);
    }
}

function closeApplicationModal() {
    const modal = document.getElementById('applicationModal');
    if (modal) {
        modal.classList.remove('is-active');
        const modalVideo = modal.querySelector('.reel-video-element');
        const modalBtn = modal.querySelector('.btn-reel-play');
        if (modalVideo && !modalVideo.paused) {
            modalVideo.pause();
            if (modalBtn) modalBtn.classList.remove('is-playing');
        }
        setTimeout(() => {
            modal.style.display = 'none';
        }, 350);
    }
}

// ==========================================================================
// 12. CONTROLADOR DE GALERÍA INTERACTIVA DE SEDES (MINIATURAS -> PRINCIPAL)
// ==========================================================================
function changeSedeGalleryImage(sedeKey, imgIndex, imgSrc, captionText) {
    const mainImg = document.getElementById(`${sedeKey}MainImg`);
    const mainCap = document.getElementById(`${sedeKey}MainCaption`);
    const panel = document.getElementById(`sede${sedeKey.charAt(0).toUpperCase() + sedeKey.slice(1)}Content`);

    if (mainImg) {
        mainImg.style.opacity = '0.2';
        setTimeout(() => {
            mainImg.src = imgSrc;
            mainImg.style.opacity = '1';
        }, 120);
    }

    if (mainCap && captionText) {
        mainCap.textContent = captionText;
    }

    if (panel) {
        const thumbs = panel.querySelectorAll('.sede-thumb-btn');
        thumbs.forEach((t, i) => {
            if (i === imgIndex) {
                t.classList.add('active');
            } else {
                t.classList.remove('active');
            }
        });
    }
}

// ==========================================================================
// 13. SLIDER ULTRA SUAVE — 6º ANIVERSARIO JD GROUP
// ==========================================================================
let currentAnniversarySlide = 0;
const totalAnniversarySlides = 2;

function setAnniversarySlide(index) {
    currentAnniversarySlide = index;
    const track = document.getElementById('anniversarySliderTrack');
    const dots = document.querySelectorAll('.anniversary-dot');

    if (track) {
        track.style.transform = `translateX(-${currentAnniversarySlide * 100}%)`;
    }

    dots.forEach((dot, i) => {
        if (i === currentAnniversarySlide) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function nextAnniversarySlide() {
    const nextIdx = (currentAnniversarySlide + 1) % totalAnniversarySlides;
    setAnniversarySlide(nextIdx);
}

function prevAnniversarySlide() {
    const prevIdx = (currentAnniversarySlide - 1 + totalAnniversarySlides) % totalAnniversarySlides;
    setAnniversarySlide(prevIdx);
}

// ==========================================================================
// 14. GATE DE ACCESO +18 (CONFIRMACIÓN DE MAYORÍA DE EDAD)
// ==========================================================================
function initAgeGate() {
    const gate = document.getElementById('ageGateModal');
    if (!gate) return;

    if (!localStorage.getItem('jdgroup_age_verified')) {
        gate.classList.add('is-active');
        document.body.style.overflow = 'hidden';
    }
}

function confirmAge() {
    localStorage.setItem('jdgroup_age_verified', 'true');
    const gate = document.getElementById('ageGateModal');
    if (gate) {
        gate.classList.remove('is-active');
        document.body.style.overflow = '';
    }
}

function rejectAge() {
    window.location.href = 'https://www.google.com';
}

// ==========================================================================
// 15. AUTO-PLAY & EFECTO POP ZOOM AL HACER SCROLL (INTERSECTION OBSERVER)
// ==========================================================================
function initScrollPopVideos() {
    const popVideos = document.querySelectorAll('.scroll-pop-reel');
    if (!popVideos.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const card = entry.target;
            const video = card.querySelector('video');
            const playBtn = card.querySelector('.btn-reel-play');

            if (entry.isIntersecting) {
                card.classList.add('is-popped');
                if (video) {
                    video.muted = true; // Auto-play requires muted
                    video.play().then(() => {
                        if (playBtn) playBtn.classList.add('is-playing');
                    }).catch(() => {});
                }
            } else {
                card.classList.remove('is-popped');
                if (video && !video.paused) {
                    video.pause();
                    if (playBtn) playBtn.classList.remove('is-playing');
                }
            }
        });
    }, { threshold: 0.40 });

    popVideos.forEach(v => observer.observe(v));
}

// ==========================================================================
// 16. CONTROLADOR DE AUDIO / SONIDO PARA VIDEOS REELS
// ==========================================================================
function toggleReelSound(btn) {
    const card = btn.closest('.video-reel-card');
    if (!card) return;
    const video = card.querySelector('video');
    if (!video) return;

    if (video.muted) {
        video.muted = false;
        video.volume = 0.85;
        btn.innerHTML = '🔊';
        btn.setAttribute('title', 'Silenciar audio');
        btn.style.borderColor = 'var(--color-champagne)';
        btn.style.color = '#FFF2D6';
        if (video.paused) {
            video.play();
            const playBtn = card.querySelector('.btn-reel-play');
            if (playBtn) playBtn.classList.add('is-playing');
        }
    } else {
        video.muted = true;
        btn.innerHTML = '🔇';
        btn.setAttribute('title', 'Activar sonido');
        btn.style.borderColor = 'rgba(183, 161, 122, 0.4)';
        btn.style.color = 'var(--color-champagne)';
    }
}

// ==========================================================================
// 17. CONTROL DE VISIBILIDAD DE MARCA DE AGUA (NO ENTRA AL HERO)
// ==========================================================================
function initFixedWatermarkVisibility() {
    const watermark = document.querySelector('.body-fixed-logo-backdrop');
    const hero = document.getElementById('actArrival');
    if (!watermark) return;

    if (!hero) {
        watermark.classList.add('is-visible');
        return;
    }

    if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.create({
            trigger: hero,
            start: "bottom 75%",
            onEnter: () => watermark.classList.add('is-visible'),
            onLeaveBack: () => watermark.classList.remove('is-visible')
        });
    } else {
        window.addEventListener('scroll', () => {
            if (window.scrollY > window.innerHeight * 0.6) {
                watermark.classList.add('is-visible');
            } else {
                watermark.classList.remove('is-visible');
            }
        });
    }
}

// ==========================================================================
// 18. GESTOR DE HOVER SUAVE DEL BOTÓN SOCIAL FLOTANTE
// ==========================================================================
function initFloatingSocialHub() {
    const hub = document.getElementById('floatingSocialHub');
    if (!hub) return;
    const trigger = hub.querySelector('.social-main-trigger');

    let closeTimeout = null;

    hub.addEventListener('mouseenter', () => {
        if (closeTimeout) clearTimeout(closeTimeout);
        hub.classList.add('is-open');
    });

    hub.addEventListener('mouseleave', () => {
        closeTimeout = setTimeout(() => {
            hub.classList.remove('is-open');
        }, 400); // 400ms buffer prevents accidental closure while moving across icons
    });

    if (trigger) {
        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            hub.classList.toggle('is-open');
        });
    }

    document.addEventListener('click', (e) => {
        if (!hub.contains(e.target)) {
            hub.classList.remove('is-open');
        }
    });
}

// ==========================================================================
// 19. NAVEGACIÓN ESPECIALIZADA PARA MÓVIL (DRAWER LUXURY)
// ==========================================================================
function toggleMobileNav(open) {
    const drawer = document.getElementById('mobileNavDrawer');
    if (!drawer) return;
    if (open) {
        drawer.classList.add('is-active');
        drawer.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    } else {
        drawer.classList.remove('is-active');
        drawer.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }
}
