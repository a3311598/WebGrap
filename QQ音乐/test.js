var window = this;
var qqMusic = {};
!function(e) {
    function t(t) {
        for (var a, n, c = t[0], i = t[1], d = t[2], l = 0, s = []; l < c.length; l++)
            n = c[l],
            Object.prototype.hasOwnProperty.call(o, n) && o[n] && s.push(o[n][0]),
            o[n] = 0;
        for (a in i)
            Object.prototype.hasOwnProperty.call(i, a) && (e[a] = i[a]);
        for (u && u(t); s.length; )
            s.shift()();
        return f.push.apply(f, d || []),
        r()
    }
    function r() {
        for (var e, t = 0; t < f.length; t++) {
            for (var r = f[t], a = !0, n = 1; n < r.length; n++) {
                var i = r[n];
                0 !== o[i] && (a = !1)
            }
            a && (f.splice(t--, 1),
            e = c(c.s = r[0]))
        }
        return e
    }
    var a = {}
      , n = {
        18: 0
    }
      , o = {
        18: 0
    }
      , f = [];
    function c(t) {
        if (a[t])
            return a[t].exports;
        var r = a[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(r.exports, r, r.exports, c),
        r.l = !0,
        r.exports
    }
    c.e = function(e) {
        var t = [];
        n[e] ? t.push(n[e]) : 0 !== n[e] && {
            1: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            19: 1,
            20: 1,
            21: 1,
            22: 1,
            23: 1
        }[e] && t.push(n[e] = new Promise((function(t, r) {
            for (var a = "css/" + ({
                1: "common",
                3: "album",
                4: "albumDetail",
                5: "album_mall",
                6: "category",
                7: "cmtpage",
                8: "index",
                9: "mv",
                10: "mvList",
                11: "mv_toplist",
                12: "notfound",
                13: "player",
                14: "playlist",
                15: "playlist_edit",
                16: "profile",
                17: "radio",
                19: "search",
                20: "singer",
                21: "singer_list",
                22: "songDetail",
                23: "toplist"
            }[e] || e) + "." + {
                1: "ce7a44036a7d9ff4c6ae",
                3: "5cf0d69eaf29bcab23d2",
                4: "798353db5b0eb05d5358",
                5: "df4c243f917604263e58",
                6: "20d532d798099a44bc88",
                7: "e3bedf2b5810f8db0684",
                8: "ea0adb959fef9011fc25",
                9: "8bdb1df6c5436b790baa",
                10: "47ce9300786df1b70584",
                11: "4aee33230ba2d6b81dce",
                12: "e6f63b0cf57dd029fbd6",
                13: "1d2dbefbea113438324a",
                14: "9484fde660fe93d9f9f0",
                15: "67fb85e7f96455763c83",
                16: "5e8c651e74b13244f7cf",
                17: "3befd83c10b19893ec66",
                19: "b2d11f89ea6a512a2302",
                20: "c7a38353c5f4ebb47491",
                21: "df0961952a2d3f022894",
                22: "4c080567e394fd45608b",
                23: "8edb142553f97482e00f"
            }[e] + ".chunk.css?max_age=2592000", o = c.p + a, f = document.getElementsByTagName("link"), i = 0; i < f.length; i++) {
                var d = (u = f[i]).getAttribute("data-href") || u.getAttribute("href");
                if ("stylesheet" === u.rel && (d === a || d === o))
                    return t()
            }
            var l = document.getElementsByTagName("style");
            for (i = 0; i < l.length; i++) {
                var u;
                if ((d = (u = l[i]).getAttribute("data-href")) === a || d === o)
                    return t()
            }
            var s = document.createElement("link");
            s.rel = "stylesheet",
            s.type = "text/css",
            s.onload = t,
            s.onerror = function(t) {
                var a = t && t.target && t.target.src || o
                  , f = new Error("Loading CSS chunk " + e + " failed.\n(" + a + ")");
                f.code = "CSS_CHUNK_LOAD_FAILED",
                f.request = a,
                delete n[e],
                s.parentNode.removeChild(s),
                r(f)
            }
            ,
            s.href = o,
            0 !== s.href.indexOf(window.location.origin + "/") && (s.crossOrigin = "anonymous"),
            document.getElementsByTagName("head")[0].appendChild(s)
        }
        )).then((function() {
            n[e] = 0
        }
        )));
        var r = o[e];
        if (0 !== r)
            if (r)
                t.push(r[2]);
            else {
                var a = new Promise((function(t, a) {
                    r = o[e] = [t, a]
                }
                ));
                t.push(r[2] = a);
                var f, i = document.createElement("script");
                i.charset = "utf-8",
                i.timeout = 120,
                c.nc && i.setAttribute("nonce", c.nc),
                i.src = function(e) {
                    return c.p + "js/" + ({
                        1: "common",
                        3: "album",
                        4: "albumDetail",
                        5: "album_mall",
                        6: "category",
                        7: "cmtpage",
                        8: "index",
                        9: "mv",
                        10: "mvList",
                        11: "mv_toplist",
                        12: "notfound",
                        13: "player",
                        14: "playlist",
                        15: "playlist_edit",
                        16: "profile",
                        17: "radio",
                        19: "search",
                        20: "singer",
                        21: "singer_list",
                        22: "songDetail",
                        23: "toplist"
                    }[e] || e) + ".chunk." + {
                        1: "c6656c0e9d51bd3fa412",
                        3: "3ad59b0dd318a4a744b3",
                        4: "c12b2aba0d6756299c13",
                        5: "37c06609fee5cfa9c5d6",
                        6: "2ef96d2c07f4be0e3cfb",
                        7: "177d8a0598269320828d",
                        8: "481eb8800765c1f86e06",
                        9: "a45514142723fef74fd3",
                        10: "704d59a3f2716b05bfa6",
                        11: "e193173e00f7c53660d5",
                        12: "f8cf98bfa861c83916b2",
                        13: "4fdd027fa838704aa564",
                        14: "1211282752c68ca37d87",
                        15: "6a038aec4034493260e0",
                        16: "25e9c2851bd9c48f10d8",
                        17: "20863af9760323626a5b",
                        19: "3bcc951fc942917576ed",
                        20: "ee96ef64b0aa6801fc62",
                        21: "ad8fbcf3d13328d12cbc",
                        22: "edc0af5299f368783f72",
                        23: "0ea1732d50a9b7c77c80"
                    }[e] + ".js?max_age=2592000"
                }(e),
                0 !== i.src.indexOf(window.location.origin + "/") && (i.crossOrigin = "anonymous");
                var d = new Error;
                f = function(t) {
                    i.onerror = i.onload = null,
                    clearTimeout(l);
                    var r = o[e];
                    if (0 !== r) {
                        if (r) {
                            var a = t && ("load" === t.type ? "missing" : t.type)
                              , n = t && t.target && t.target.src;
                            d.message = "Loading chunk " + e + " failed.\n(" + a + ": " + n + ")",
                            d.name = "ChunkLoadError",
                            d.type = a,
                            d.request = n,
                            r[1](d)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function() {
                    f({
                        type: "timeout",
                        target: i
                    })
                }
                ), 12e4);
                i.onerror = i.onload = f,
                document.head.appendChild(i)
            }
        return Promise.all(t)
    }
    ,
    c.m = e,
    c.c = a,
    c.d = function(e, t, r) {
        c.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: r
        })
    }
    ,
    c.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    c.t = function(e, t) {
        if (1 & t && (e = c(e)),
        8 & t)
            return e;
        if (4 & t && "object" === typeof e && e && e.__esModule)
            return e;
        var r = Object.create(null);
        if (c.r(r),
        Object.defineProperty(r, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var a in e)
                c.d(r, a, function(t) {
                    return e[t]
                }
                .bind(null, a));
        return r
    }
    ,
    c.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return c.d(t, "a", t),
        t
    }
    ,
    c.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    c.p = "/ryqq/",
    c.oe = function(e) {
        throw e
    }
    ;
    var i = window.webpackJsonp = window.webpackJsonp || []
      , d = i.push.bind(i);
    i.push = t,
    i = i.slice();
    for (var l = 0; l < i.length; l++)
        t(i[l]);
    var u = d;
    r()
    qqMusic = c;
}(
    {

        350:function(e, t, n) {
    "use strict";
    n.r(t),
    function(e) {
        var n = "undefined" !== typeof e ? e : "undefined" !== typeof window ? window : "undefined" !== typeof self ? self : void 0;
        var r = function() {
            function e(t, n, r, i, o, a, u, l) {
                var c = !i;
                t = +t,
                n = n || [0],
                i = i || [[this], [{}]],
                o = o || {};
                var s, f = [], p = null;
                Function.prototype.bind || (s = [].slice,
                Function.prototype.bind = function(e) {
                    if ("function" != typeof this)
                        throw new TypeError("bind101");
                    var t = s.call(arguments, 1)
                      , n = t.length
                      , r = this
                      , i = function() {}
                      , o = function() {
                        return t.length = n,
                        t.push.apply(t, arguments),
                        r.apply(i.prototype.isPrototypeOf(this) ? this : e, t)
                    };
                    return this.prototype && (i.prototype = this.prototype),
                    o.prototype = new i,
                    o
                }
                );
                for (var d = [function() {
                    i[i.length - 2] = i[i.length - 2] + i.pop()
                }
                , function() {
                    for (var a = n[t++], u = [], l = n[t++], c = n[t++], s = [], f = 0; f < l; f++)
                        u[n[t++]] = i[n[t++]];
                    for (f = 0; f < c; f++)
                        s[f] = n[t++];
                    i.push((function t() {
                        var i = u.slice(0);
                        i[0] = [this],
                        i[1] = [arguments],
                        i[2] = [t];
                        for (var l = 0; l < s.length && l < arguments.length; l++)
                            0 < s[l] && (i[s[l]] = [arguments[l]]);
                        return e(a, n, r, i, o)
                    }
                    ))
                }
                , function() {
                    i[i.length - 2] = i[i.length - 2] | i.pop()
                }
                , function() {
                    i.push(i[n[t++]][0])
                }
                , function() {
                    var e = n[t++]
                      , r = i[i.length - 2 - e];
                    i[i.length - 2 - e] = i.pop(),
                    i.push(r)
                }
                , , function() {
                    var e = n[t++]
                      , r = e ? i.slice(-e) : [];
                    i.length -= e,
                    e = i.pop(),
                    i.push(e[0][e[1]].apply(e[0], r))
                }
                , , , function() {
                    var e = n[t++];
                    i[i.length - 1] && (t = e)
                }
                , function() {
                    var e = n[t++]
                      , r = e ? i.slice(-e) : [];
                    i.length -= e,
                    r.unshift(null),
                    i.push(function() {
                        return function(e, t, n) {
                            return new (Function.bind.apply(e, t))
                        }
                        .apply(null, arguments)
                    }(i.pop(), r))
                }
                , function() {
                    i[i.length - 2] = i[i.length - 2] - i.pop()
                }
                , function() {
                    var e = i[i.length - 2];
                    e[0][e[1]] = i[i.length - 1]
                }
                , , function() {
                    var e = n[t++];
                    i[e] = void 0 === i[e] ? [] : i[e]
                }
                , , function() {
                    i.push(!i.pop())
                }
                , , , , function() {
                    i.push([n[t++]])
                }
                , function() {
                    i[i.length - 1] = r[i[i.length - 1]]
                }
                , , function() {
                    i.push("")
                }
                , , function() {
                    i[i.length - 2] = i[i.length - 2] << i.pop()
                }
                , , function() {
                    var e = i.pop();
                    i.push([i[i.pop()][0], e])
                }
                , function() {
                    i.push(i[i.pop()[0]][0])
                }
                , , function() {
                    i[i.length - 1] = n[t++]
                }
                , function() {
                    i[i.length - 2] = i[i.length - 2] >> i.pop()
                }
                , , function() {
                    i.push(!1)
                }
                , function() {
                    i[i.length - 2] = i[i.length - 2] > i.pop()
                }
                , , function() {
                    i[i.length - 2] = i[i.length - 2] ^ i.pop()
                }
                , function() {
                    i.push([i.pop(), i.pop()].reverse())
                }
                , function() {
                    i.pop()
                }
                , function() {
                    i[i[i.length - 2][0]][0] = i[i.length - 1]
                }
                , , , , function() {
                    i.push(i[i.length - 1])
                }
                , , function() {
                    return !0
                }
                , function() {
                    i.push([r, i.pop()])
                }
                , function() {
                    var e = n[t++]
                      , o = e ? i.slice(-e) : [];
                    i.length -= e,
                    i.push(i.pop().apply(r, o))
                }
                , function() {
                    i[i.length - 2] = i[i.length - 2] >= i.pop()
                }
                , , , function() {
                    i.length = n[t++]
                }
                , , function() {
                    var e = i.pop()
                      , t = i.pop();
                    i.push([t[0][t[1]], e])
                }
                , , function() {
                    i[i.length - 2] = i[i.length - 2] & i.pop()
                }
                , function() {
                    t = n[t++]
                }
                , , function() {
                    i[i.length - 1] += String.fromCharCode(n[t++])
                }
                , , , function() {
                    i[i.length - 2] = i[i.length - 2] === i.pop()
                }
                , function() {
                    i.push(void 0)
                }
                , function() {
                    var e = i.pop();
                    i.push(e[0][e[1]])
                }
                , , function() {
                    i.push(!0)
                }
                , , function() {
                    i[i.length - 2] = i[i.length - 2] * i.pop()
                }
                , function() {
                    i.push(n[t++])
                }
                , function() {
                    i.push(typeof i.pop())
                }
                ]; ; )
                    try {
                        for (var h = !1; !h; )
                            h = d[n[t++]]();
                        if (p)
                            throw p;
                        return c ? (i.pop(),
                        i.slice(3 + e.v)) : i.pop()
                    } catch (m) {
                        var v = f.pop();
                        if (void 0 === v)
                            throw m;
                        p = m,
                        t = v[0],
                        i.length = v[1],
                        v[2] && (i[v[2]][0] = p)
                    }
            }
            return e.v = 5,
            e(0, function(e) {
                var t = e[1]
                  , n = []
                  , r = function(e) {
                    for (var t, n, r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".split(""), i = String(e).replace(/[=]+$/, ""), o = 0, a = 0, u = ""; n = i.charAt(a++); ~n && (t = o % 4 ? 64 * t + n : n,
                    o++ % 4) && (u += String.fromCharCode(255 & t >> (-2 * o & 6))))
                        n = function(e, t, n) {
                            if ("function" == typeof Array.prototype.indexOf)
                                return Array.prototype.indexOf.call(e, t, n);
                            var r;
                            if (null == e)
                                throw new TypeError('"array" is null or not defined');
                            var i = Object(e)
                              , o = i.length >>> 0;
                            if (0 == o)
                                return -1;
                            if (o <= (n |= 0))
                                return -1;
                            for (r = Math.max(0 <= n ? n : o - Math.abs(n), 0); r < o; r++)
                                if (r in i && i[r] === t)
                                    return r;
                            return -1
                        }(r, n);
                    return u
                }(e[0])
                  , i = t.shift()
                  , o = t.shift()
                  , a = 0;
                function u() {
                    for (; a === i; )
                        n.push(o),
                        a++,
                        i = t.shift(),
                        o = t.shift()
                }
                for (var l = 0; l < r.length; l++) {
                    var c = r.charAt(l).charCodeAt(0);
                    u(),
                    n.push(c),
                    a++
                }
                return u(),
                n
            }(["MwgOAg4DDgQOBQ4GDgc4fzozCQ4CDgMOBA4FDgYOBw4IFzpkOmU6ZjppOm46ZRVFFzpmOnU6bjpjOnQ6aTpvOm49CUc4XzomFzpkOmU6ZjppOm46ZS4XOmE6bTpkNT8JaSYDAy8AOHwJJhc6ZDplOmY6aTpuOmUuAwMGASY+LQERAAEDOAMzCg4CDgMOBA4FDgYOBw4IDgkUCDg8MwgOAg4DDgQOBQ4GDgcXOmc6bDpvOmI6YTpsFUUXOnU6bjpkOmU6ZjppOm46ZTpkPRAJ1iY45gQmFzpnOmw6bzpiOmE6bBUtFzp3Omk6bjpkOm86dxVFFzp1Om46ZDplOmY6aTpuOmU6ZD0QCSY4BiYXOnc6aTpuOmQ6bzp3FS0XOnM6ZTpsOmYVRRc6dTpuOmQ6ZTpmOmk6bjplOmQ9EAkmOAEmFzpzOmU6bDpmFS0+LQGeAAAvACcmJhQJOA0zIg4CDgMOBA4FDgYOBw4IDgkOCg4LDgwODQ4ODg8OEA4RDhIOEw4UDhUOFg4XDhgOGQ4aDhsOHA4dDh4OHw4gFAkXOk86YjpqOmU6Yzp0FQoAKxc6MCVEAAwmJisXOjElRAEMJiYrFzoyJUQCDCYmKxc6MyVEAwwmJisXOjQlRAQMJiYrFzo1JUQFDCYmKxc6NiVEBgwmJisXOjclRAcMJiYrFzo4JUQIDCYmKxc6OSVECQwmJisXOkElRAoMJiYrFzpCJUQLDCYmKxc6QyVEDAwmJisXOkQlRA0MJiYrFzpFJUQODCYmKxc6RiVEI0QUCwwmJicmJhQKFzpBOkI6QzpEOkU6RjpHOkg6STpKOks6TDpNOk46TzpQOlE6UjpTOlQ6VTpWOlc6WDpZOlo6YTpiOmM6ZDplOmY6ZzpoOmk6ajprOmw6bTpuOm86cDpxOnI6czp0OnU6djp3Ong6eTp6OjA6MToyOjM6NDo1OjY6Nzo4Ojk6KzovOj0nJiYUCxQhFzpfOl86czppOmc6bjpfOmg6YTpzOmg6XzoyOjA6MjowOjA6MzowOjUbPwk4MyYhFCEXOl86XzpzOmk6ZzpuOl86aDphOnM6aDpfOjI6MDoyOjA6MDozOjA6NRsDAwYBBAAmFzp0Om86VTpwOnA6ZTpyOkM6YTpzOmUlBgAnJiYUDBc6dzppOm46ZDpvOncVRRc6bzpiOmo6ZTpjOnQ9CTgBJhc6bjphOnY6aTpnOmE6dDpvOnIVRRc6bzpiOmo6ZTpjOnQ9CTgDJhc6bDpvOmM6YTp0Omk6bzpuFUUXOm86YjpqOmU6Yzp0PScmJhQNAwwJOAomFzpSOmU6ZzpFOng6cBUXOkg6ZTphOmQ6bDplOnM6cxc6aS8CFzp0OmU6czp0JRc6bjphOnY6aTpnOmE6dDpvOnIuFzp1OnM6ZTpyOkE6ZzplOm46dDU/BgEnJiYUDhQhFzpfOl86cTptOmY6ZTpfOnM6aTpnOm46XzpjOmg6ZTpjOmsbP0QBPQkmAwwJOAkmAw0QCTg4Jhc6bDpvOmM6YTp0Omk6bzpuLhc6aDpvOnM6dDUXOmk6bjpkOmU6eDpPOmY1FzpxOnE6LjpjOm86bQYBRABEAQsiJyYmFA9BFzpBOnI6cjphOnkVCgArRAAlRC5EGQsMJiYrRAElRAQMJiYrRAIlRAkMJiYrRAMlRDVEGwsMJiYrRAQlRANEDQAMJiYrRAUlRABEFAAMJiYrRAYlRC9EFAsMJiYrRAclRC9EEQsMJiYXOm06YTpwJTgBMwsOAg4DDgQOBQ4GDgcOCBQJAwoJJgMDRAEAOAomAwMbPy0BAgEJCwoOAwYBFzpqOm86aTpuJQQAJhcGAScmJhQQFzpBOnI6cjphOnkVCgArRAAlRAZEDAAMJiYrRAElRAsMJiYrRAIlRAMMJiYrRAMlRAIMJiYrRAQlRAEMJiYrRAUlRAcMJiYrRAYlRAYMJiYrRAclRDlEIAsMJiYXOm06YTpwJTgxMwsOAg4DDgQOBQ4GDgcOCBQJAwoJJgMDRAEAOAEmAwMbPy0BAgEJCwoOAwYBFzpqOm86aTpuJRcGAScmJhQRFzpBOnI6cjphOnkVCgArRAAlRAhEEUQMQwAMJiYrRAElRAtEIgAMJiYrRAIlRDREHAAMJiYrRAMlRDxECAAMJiYrRAQlRA1EDkQNQwAMJiYrRAUlRAdEDEQNQwAMJiYrRAYlRAdEDUQMQwAMJiYrRAclRAtEEEQMQwAMJiYrRAglRAVECEQTQwAMJiYrRAklRApEDkQPQwAMJiYrRAolRBBEEUQOQwAMJiYrRAslRB1EPgAMJiYrRAwlRAxEEUMMJiYrRA0lRApERQAMJiYrRA4lRAdEYQAMJiYrRDxELQslRAYMJiYnJiYDDhAJJjgeJhQRFzpBOnI6cjphOnkVCgArRAAlRBVEBAAMJiYrRAElRBtEJwAMJiYrRAIlRAEMJiYrRAMlRDhEAgAMJiYrRAQlRANEVwAMJiYrRAUlRDVEGQAMJiYrRAYlRDlEQgAMJiYrRAclRBpELQAMJiYrRAglRCVEBAsMJiYrRAklRAwMJiYrRAolRAhECkQRQwAMJiYrRAslRDJEKwAMJiYrRAwlRCFEBwAMJiYrRA0lRApEDEQNQwAMJiYrRA4lRC5EEAAMJiYrRBFEAgslRAhED0QPQwAMJiYnJiYUEhc6QTpyOnI6YTp5FQoAJyYmFBNEACcmJhQTHEQTRAMLMBAJJjgUJhQUFAkUCwMTRAJDGz8bP0Q2RCYLQxQJFAsDE0QCQ0QBABs/Gz8AJyYmFBUUEQMTGz8nJiYUEhc6cDp1OnM6aBsDFAMVJAYBJhQTKxwrBAEEAEQBACcmHgAEAAImOEQUERQLFAkhJwQAJicEACYnJiYUHRcnJiYUHkQAJyYmFB4cRAUwEAkmOBQmFBYUEgMeRANDGz8nJiYUFxQSAx5EA0NEAQAbPycmJhQYFBIDHkQDQ0QCABs/JyYmFBkDFkQCHycmJhQaAxZEAzdEBBkDF0QEHwInJiYUGwMXRAVECgA3RAIZAxhEBh8CJyYmFBwDGEQ1RAoANycmJhQdAx0UCgMZGz8AFAoDGhs/ABQKAxsbPwAUCgMcGz8AJyYmFB4rHCsEAQQARAEAJyYeAAQAAiY4LxQdAx0UChQSRAhEBwAbP0QCHxs/ABQKFBJEC0QEABs/RAM3RAQZGz8AJyYmFBIhJyYmFB8UHRc6cjplOnA6bDphOmM6ZRsXOlI6ZTpnOkU6eDpwFRc6WzpcOi86KzpdFzpnLwIXBgInJiYUIBc6ejp6OmIDDwADHwADEAAnJiYUDxQQFB8UHRQKIScEACYnBAAmJwQAJicEACYnJiYUIBc6dDpvOkw6bzp3OmU6cjpDOmE6czplGwYALQEBASEIAycmJhQIFzpfOmc6ZTp0OlM6ZTpjOnU6cjppOnQ6eTpTOmk6ZzpuGwMJDCYmPi0BhwAALwEmPi0=", [133, 2628, 156, 340, 267, 272, 270, 288, 321, 326, 324, 338, 352, 2575, 786, 790, 788, 869, 904, 908, 906, 944, 945, 949, 947, 983, 991, 995, 993, 1085, 1133, 1217, 1138, 1142, 1140, 1146, 1147, 1151, 1149, 1217, 1336, 1375, 1359, 1369, 1367, 1372, 1376, 1338, 1508, 1547, 1531, 1541, 1539, 1544, 1548, 1510, 1813, 1818, 1816, 2036, 2073, 2078, 2076, 2174, 2172, 2062, 2213, 2218, 2216, 2389, 2387, 2205, 2576, 354]]), n)
        }();
        r.g = function() {
            return r.shift()[0]
        }
        ,
        n.__sign_hash_20200305 = function(e) {
            function t(e, t) {
                var n = (65535 & e) + (65535 & t);
                return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
            }
            function n(e, n, r, i, o, a) {
                return t((u = t(t(n, e), t(i, a))) << (l = o) | u >>> 32 - l, r);
                var u, l
            }
            function r(e, t, r, i, o, a, u) {
                return n(t & r | ~t & i, e, t, o, a, u)
            }
            function i(e, t, r, i, o, a, u) {
                return n(t & i | r & ~i, e, t, o, a, u)
            }
            function o(e, t, r, i, o, a, u) {
                return n(t ^ r ^ i, e, t, o, a, u)
            }
            function a(e, t, r, i, o, a, u) {
                return n(r ^ (t | ~i), e, t, o, a, u)
            }
            function u(e) {
                return function(e) {
                    var t, n = "";
                    for (t = 0; t < 32 * e.length; t += 8)
                        n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
                    return n
                }(function(e, n) {
                    e[n >> 5] |= 128 << n % 32,
                    e[14 + (n + 64 >>> 9 << 4)] = n;
                    var u, l, c, s, f, p = 1732584193, d = -271733879, h = -1732584194, v = 271733878;
                    for (u = 0; u < e.length; u += 16)
                        l = p,
                        c = d,
                        s = h,
                        f = v,
                        p = r(p, d, h, v, e[u], 7, -680876936),
                        v = r(v, p, d, h, e[u + 1], 12, -389564586),
                        h = r(h, v, p, d, e[u + 2], 17, 606105819),
                        d = r(d, h, v, p, e[u + 3], 22, -1044525330),
                        p = r(p, d, h, v, e[u + 4], 7, -176418897),
                        v = r(v, p, d, h, e[u + 5], 12, 1200080426),
                        h = r(h, v, p, d, e[u + 6], 17, -1473231341),
                        d = r(d, h, v, p, e[u + 7], 22, -45705983),
                        p = r(p, d, h, v, e[u + 8], 7, 1770035416),
                        v = r(v, p, d, h, e[u + 9], 12, -1958414417),
                        h = r(h, v, p, d, e[u + 10], 17, -42063),
                        d = r(d, h, v, p, e[u + 11], 22, -1990404162),
                        p = r(p, d, h, v, e[u + 12], 7, 1804603682),
                        v = r(v, p, d, h, e[u + 13], 12, -40341101),
                        h = r(h, v, p, d, e[u + 14], 17, -1502002290),
                        p = i(p, d = r(d, h, v, p, e[u + 15], 22, 1236535329), h, v, e[u + 1], 5, -165796510),
                        v = i(v, p, d, h, e[u + 6], 9, -1069501632),
                        h = i(h, v, p, d, e[u + 11], 14, 643717713),
                        d = i(d, h, v, p, e[u], 20, -373897302),
                        p = i(p, d, h, v, e[u + 5], 5, -701558691),
                        v = i(v, p, d, h, e[u + 10], 9, 38016083),
                        h = i(h, v, p, d, e[u + 15], 14, -660478335),
                        d = i(d, h, v, p, e[u + 4], 20, -405537848),
                        p = i(p, d, h, v, e[u + 9], 5, 568446438),
                        v = i(v, p, d, h, e[u + 14], 9, -1019803690),
                        h = i(h, v, p, d, e[u + 3], 14, -187363961),
                        d = i(d, h, v, p, e[u + 8], 20, 1163531501),
                        p = i(p, d, h, v, e[u + 13], 5, -1444681467),
                        v = i(v, p, d, h, e[u + 2], 9, -51403784),
                        h = i(h, v, p, d, e[u + 7], 14, 1735328473),
                        p = o(p, d = i(d, h, v, p, e[u + 12], 20, -1926607734), h, v, e[u + 5], 4, -378558),
                        v = o(v, p, d, h, e[u + 8], 11, -2022574463),
                        h = o(h, v, p, d, e[u + 11], 16, 1839030562),
                        d = o(d, h, v, p, e[u + 14], 23, -35309556),
                        p = o(p, d, h, v, e[u + 1], 4, -1530992060),
                        v = o(v, p, d, h, e[u + 4], 11, 1272893353),
                        h = o(h, v, p, d, e[u + 7], 16, -155497632),
                        d = o(d, h, v, p, e[u + 10], 23, -1094730640),
                        p = o(p, d, h, v, e[u + 13], 4, 681279174),
                        v = o(v, p, d, h, e[u], 11, -358537222),
                        h = o(h, v, p, d, e[u + 3], 16, -722521979),
                        d = o(d, h, v, p, e[u + 6], 23, 76029189),
                        p = o(p, d, h, v, e[u + 9], 4, -640364487),
                        v = o(v, p, d, h, e[u + 12], 11, -421815835),
                        h = o(h, v, p, d, e[u + 15], 16, 530742520),
                        p = a(p, d = o(d, h, v, p, e[u + 2], 23, -995338651), h, v, e[u], 6, -198630844),
                        v = a(v, p, d, h, e[u + 7], 10, 1126891415),
                        h = a(h, v, p, d, e[u + 14], 15, -1416354905),
                        d = a(d, h, v, p, e[u + 5], 21, -57434055),
                        p = a(p, d, h, v, e[u + 12], 6, 1700485571),
                        v = a(v, p, d, h, e[u + 3], 10, -1894986606),
                        h = a(h, v, p, d, e[u + 10], 15, -1051523),
                        d = a(d, h, v, p, e[u + 1], 21, -2054922799),
                        p = a(p, d, h, v, e[u + 8], 6, 1873313359),
                        v = a(v, p, d, h, e[u + 15], 10, -30611744),
                        h = a(h, v, p, d, e[u + 6], 15, -1560198380),
                        d = a(d, h, v, p, e[u + 13], 21, 1309151649),
                        p = a(p, d, h, v, e[u + 4], 6, -145523070),
                        v = a(v, p, d, h, e[u + 11], 10, -1120210379),
                        h = a(h, v, p, d, e[u + 2], 15, 718787259),
                        d = a(d, h, v, p, e[u + 9], 21, -343485551),
                        p = t(p, l),
                        d = t(d, c),
                        h = t(h, s),
                        v = t(v, f);
                    return [p, d, h, v]
                }(function(e) {
                    var t, n = [];
                    for (n[(e.length >> 2) - 1] = void 0,
                    t = 0; t < n.length; t += 1)
                        n[t] = 0;
                    for (t = 0; t < 8 * e.length; t += 8)
                        n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
                    return n
                }(e), 8 * e.length))
            }
            function l(e) {
                return u(unescape(encodeURIComponent(e)))
            }
            return function(e) {
                var t, n, r = "";
                for (n = 0; n < e.length; n += 1)
                    t = e.charCodeAt(n),
                    r += "0123456789abcdef".charAt(t >>> 4 & 15) + "0123456789abcdef".charAt(15 & t);
                return r
            }(l(e))
        }
        ;
        var i = n._getSecuritySign;
        delete n._getSecuritySign,
        t.default = i
    }
    .call(this, n(110))
},
        110:function(e, t) {
            var n;
            n = function() {
                return this
            }();
            try {
                n = n || new Function("return this")()
            } catch (r) {
                "object" === typeof window && (n = window)
            }
            e.exports = n
        }
    }

);


var y = {
    "isBrowser": true,
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "version": 0,
    "client": "pc"
}
var e = {
    "data": {
        "comm": {
            "cv": 4747474,
            "ct": 24,
            "format": "json",
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
            "platform": "yqq.json",
            "needNewCode": 1,
            "uin": 799129490,
            "g_tk_new_20200303": 946290626,
            "g_tk": 946290626
        },
        "req_1": {
            "module": "userInfo.VipQueryServer",
            "method": "SRFVipQuery_V2",
            "param": {
                "uin_list": [
                    "799129490"
                ]
            }
        },
        "req_2": {
            "module": "userInfo.BaseUserInfoServer",
            "method": "get_user_baseinfo_v2",
            "param": {
                "vec_uin": [
                    "799129490"
                ]
            }
        },
        "req_3": {
            "module": "vkey.GetVkeyServer",
            "method": "CgiGetVkey",
            "param": {
                "guid": "6650390648",
                "songmid": [
                    "001zLvbN1NYMuv",
                    "004DXFlC0nsTCZ"
                ],
                "songtype": [
                    0,
                    0
                ],
                "uin": "799129490",
                "loginflag": 1,
                "platform": "20"
            }
        },
        "req_4": {
            "module": "music.musicasset.SongFavRead",
            "method": "IsSongFanByMid",
            "param": {
                "v_songMid": [
                    "001zLvbN1NYMuv",
                    "000NqZLy2lfXjT",
                    "004DXFlC0nsTCZ",
                    "001bo9Wy1NfHpb"
                ]
            }
        },
        "req_5": {
            "method": "GetCommentCount",
            "module": "music.globalComment.GlobalCommentRead",
            "param": {
                "request_list": [
                    {
                        "biz_type": 1,
                        "biz_id": "244625442",
                        "biz_sub_type": 0
                    }
                ]
            }
        },
        "req_6": {
            "module": "music.musichallAlbum.AlbumInfoServer",
            "method": "GetAlbumDetail",
            "param": {
                "albumMid": "0037Yq3H3RznaX"
            }
        },
        "req_7": {
            "module": "vkey.GetVkeyServer",
            "method": "CgiGetVkey",
            "param": {
                "guid": "6989760652",
                "songmid": [
                    "001zLvbN1NYMuv"
                ],
                "songtype": [
                    0
                ],
                "uin": "799129490",
                "loginflag": 1,
                "platform": "20"
            }
        }
    },
    "time": 10000,
    "withCredentials": true,
    "cache": false,
    "url": "//u.y.qq.com/cgi-bin/musicu.fcg",
    "postType": true,
    "type": "POST",
    "needSign": true


}


var F = {
        type: "GET",
        data: {},
        dataType: "json",
        beforeSend: null,
        success: null,
        error: null,
        complete: null,
        accepts: {
            script: "text/javascript, application/javascript, application/x-javascript",
            json: "application/json",
            xml: "application/xml, text/xml",
            html: "text/html",
            text: "text/plain"
        },
        crossDomain: !0,
        time: 0
    }
function A(e, t) {
        if (t = t || window.location.href,
        "object" !== typeof e && !e)
            return t;
        var n = e;
        return "object" === typeof e && (n = [],
        Object.keys(e).forEach((function(t) {
            n.push(encodeURIComponent(t) + "=" + encodeURIComponent(e[t]))
        }
        )),
        n = n.join("&")),
        t = /\?/.test(t) || /#/.test(t) ? /\?/.test(t) && !/#/.test(t) ? t + "&" + n : !/\?/.test(t) && /#/.test(t) ? t.replace("#", "?" + n + "#") : t.replace("?", "?" + n + "&") : t + "?" + n
    }
function b(e) {
        return "[object Object]" === Object.prototype.toString.call(e)
    }
function E(e) {
        return b(e) && null !== e && e !== e.window && Object.getPrototypeOf(e) === Object.prototype
    }
function _(e) {
        for (var t, n = !1, r = arguments.length, i = new Array(r > 1 ? r - 1 : 0), o = 1; o < r; o++)
            i[o - 1] = arguments[o];
        "boolean" === typeof e ? (n = e,
        t = i.shift()) : t = e;
        var a = function e(t, n, r) {
            Object.keys(n).forEach((function(i) {
                var o = n[i];
                r && E(o) || Array.isArray(o) ? (E(o) && !E(t[i]) && (t[i] = {}),
                Array.isArray(n[i]) && !Array.isArray(t[i]) && (t[i] = []),
                e(t[i], n[i], r)) : void 0 !== o && (t[i] = o)
            }
            ))
        };
        return i.forEach((function(e) {
            a(t, e, n)
        }
        )),
        t
    }

function L(e) {
        var t = _(!0, {}, F, e)
          , r = t.dataType.toLowerCase();
        if (t.url = A({
            _: Date.now()
        }, t.url),
        "GET" === t.type.toUpperCase() ? (t.url = A(t.data, t.url),
        t.data = void 0) : "string" === typeof t.data || (t.data = JSON.stringify(t.data)),
        t.needSign && -1 !== t.url.indexOf("cgi-bin/musicu.fcg") && y.isBrowser && (t.url = t.url.replace("cgi-bin/musicu.fcg", "cgi-bin/musics.fcg")),
        -1 !== t.url.indexOf("cgi-bin/musics.fcg")) {
            var i, o = qqMusic(350).default;
            console.log(i, o(t.data));
            i = "GET" === t.type.toUpperCase() ? o(t.data.data) : o(t.data),
            t.url = A({
                sign: i
            }, t.url)

        }
        var a, u = F.accepts[r], l = {}, c = /^([\w-]+:)\/\//.test(t.url) ? RegExp.$1 : window.location.protocol, s = new XMLHttpRequest;
        if (l.Accept = u || "*/*",
        !t.crossDomain) {
            var f = document.createElement("a");
            f.href = t.url,
            t.crossDomain = g.protocol + "//" + g.host !== f.protocol + "//" + f.host,
            l["X-Requested-With"] = "XMLHttpRequest"
        }
        if (t.mimeType) {
            if ((u = t.mimeType).indexOf(",") > -1) {
                var p = u.split(",", 2);
                u = p[0]
            }
            s.overrideMimeType && s.overrideMimeType(u)
        }
        return (t.contentType || t.data && "GET" !== t.type.toUpperCase() && !(t.data instanceof FormData)) && (l["Content-Type"] = t.contentType || "application/x-www-form-urlencoded"),
        l = Object.assign(l, t.headers),
        new Promise((function(e, n) {
            s.onreadystatechange = function() {
                if (4 === s.readyState) {
                    clearTimeout(a);
                    var t = null
                      , r = null;
                    if (s.status >= 200 && s.status <= 300 || 304 === s.status || 0 === s.status && "file:" === c) {
                        var i = u || s.getResponseHeader("content-type");
                        r = s.responseText;
                        try {
                            /^(?:text|application)\/xml/i.test(i) ? r = s.responseXML : "application/json" === i && (r = /^\s*$/.test(r) ? null : JSON.parse(r))
                        } catch (at) {
                            t = at
                        }
                        t ? n({
                            error: t,
                            xhr: s
                        }) : e({
                            result: r,
                            xhr: s
                        })
                    } else
                        n({
                            error: t,
                            xhr: s
                        })
                }
            }
            ,
            t.beforeSend && !1 === t.beforeSend() ? s.abort() : (s.open(t.type, t.url, t.async || !0, t.username, t.password),
            t.withCredentials && (s.withCredentials = !0),
            Object.keys(l).forEach((function(e) {
                s.setRequestHeader(e, l[e])
            }
            )),
            t.time > 0 && (a = setTimeout((function() {
                s.abort()
            }
            ), t.time)),
            s.send(t.data || null))
        }
        ))
};

console.log(L(e))