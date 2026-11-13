/* Course pages: progress, quiz feedback and theme toggle. No network calls; storage is optional. */
(function () {
  "use strict";
  var PREFIX = "lpc-course:";
  function read(key) { try { return window.localStorage.getItem(PREFIX + key); } catch (e) { return null; } }
  function write(key, value) { try { window.localStorage.setItem(PREFIX + key, value); return true; } catch (e) { return false; } }
  function remove(key) { try { window.localStorage.removeItem(PREFIX + key); } catch (e) { /* storage unavailable */ } }

  /* theme */
  var themeKey = "theme", saved = read(themeKey);
  if (saved === "light" || saved === "dark") document.documentElement.setAttribute("data-theme", saved);
  var tt = document.querySelector("[data-theme-toggle]");
  if (tt) tt.addEventListener("click", function () {
    var cur = document.documentElement.getAttribute("data-theme") ||
      (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    write(themeKey, next);
    tt.setAttribute("aria-pressed", next === "dark" ? "true" : "false");
  });

  /* "mark as done" buttons: data-mark="<key>" */
  document.querySelectorAll("[data-mark]").forEach(function (btn) {
    var key = btn.getAttribute("data-mark");
    function paint() {
      var on = read(key) === "done";
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      btn.textContent = on ? btn.getAttribute("data-label-on") : btn.getAttribute("data-label-off");
    }
    btn.addEventListener("click", function () {
      if (read(key) === "done") remove(key); else write(key, "done");
      paint();
    });
    paint();
  });

  /* progress bars and per-item ticks: data-keys="k1 k2 ..." */
  document.querySelectorAll("[data-progress]").forEach(function (el) {
    var keys = (el.getAttribute("data-progress") || "").split(" ").filter(Boolean);
    var done = keys.filter(function (k) { return read(k) === "done" || (read(k) || "").indexOf("score:") === 0; }).length;
    var pct = keys.length ? Math.round(100 * done / keys.length) : 0;
    var bar = el.querySelector(".bar > span"), txt = el.querySelector(".pct");
    if (bar) bar.style.width = pct + "%";
    if (txt) txt.textContent = done + " of " + keys.length + " done (" + pct + "%)";
    var meter = el.querySelector("[role=progressbar]");
    if (meter) meter.setAttribute("aria-valuenow", String(pct));
  });
  document.querySelectorAll("[data-tick]").forEach(function (el) {
    var v = read(el.getAttribute("data-tick"));
    if (v === "done" || (v || "").indexOf("score:") === 0) { el.textContent = "✓"; el.setAttribute("title", "done"); el.setAttribute("aria-label", "done"); }
  });

  /* quizzes */
  var form = document.querySelector("form[data-quiz]");
  if (form) {
    var dataEl = document.getElementById("quiz-data"), bank = [];
    try { bank = JSON.parse(dataEl.textContent).questions; } catch (e) { bank = []; }
    var key = form.getAttribute("data-quiz"), scoreEl = document.getElementById("quiz-score"), results = {};
    function grade(i) {
      var q = bank[i], box = form.querySelector('[data-q="' + i + '"]');
      var picked = Array.prototype.map.call(box.querySelectorAll("input:checked"), function (n) { return parseInt(n.value, 10); }).sort();
      if (!picked.length) return;
      var want = q.answer.slice().sort(), ok = picked.length === want.length && picked.every(function (v, k) { return v === want[k]; });
      results[i] = ok;
      box.classList.remove("right", "wrong"); box.classList.add(ok ? "right" : "wrong");
      var fb = box.querySelector(".fb");
      fb.className = "fb " + (ok ? "right" : "wrong");
      fb.textContent = (ok ? "Correct. " : "Not quite. ") + q.explain;
      var answered = Object.keys(results).length, right = Object.keys(results).filter(function (k) { return results[k]; }).length;
      scoreEl.textContent = "Score: " + right + " of " + bank.length + " (" + answered + " answered)";
      if (answered === bank.length) write(key, "score:" + right + "/" + bank.length);
    }
    form.querySelectorAll("[data-q]").forEach(function (box) {
      var i = parseInt(box.getAttribute("data-q"), 10), multi = box.getAttribute("data-multi") === "1";
      if (multi) {
        var b = box.querySelector("button[data-check]");
        b.addEventListener("click", function () { grade(i); });
      } else {
        box.addEventListener("change", function () { grade(i); });
      }
    });
    var reset = document.getElementById("quiz-reset");
    if (reset) reset.addEventListener("click", function () {
      results = {}; form.reset();
      form.querySelectorAll("[data-q]").forEach(function (b) { b.classList.remove("right", "wrong"); var f = b.querySelector(".fb"); f.className = "fb"; f.textContent = ""; });
      scoreEl.textContent = ""; remove(key);
    });
    var prev = read(key);
    if (prev && prev.indexOf("score:") === 0) scoreEl.textContent = "Last completed score: " + prev.slice(6) + ".";
  }
})();
