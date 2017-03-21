# coding:utf-8
import execjs
import random

ctx = execjs.compile("""
    function ra(a, b) {
        for (var c = b.slice(32), d = [], e = 0; e < c.length; e++) {
            var f = c.charCodeAt(e);
            d[e] = f > 57 ? f - 87 : f - 48
        }
        c = 36 * d[0] + d[1];
        var g = Math.round(a) + c;
        b = b.slice(0, 32);
        var h, i = [
                [],
                [],
                [],
                [],
                []
            ],
            j = {},
            k = 0;
        e = 0;
        for (var l = b.length; e < l; e++)
            h = b.charAt(e), j[h] || (j[h] = 1, i[k].push(h), k++, k = 5 == k ? 0 : k);
        for (var m, n = g, o = 4, p = "", q = [1, 2, 5, 10, 50]; n > 0;)
            n - q[o] >= 0 ? (m = parseInt(Math.random() * i[o].length, 10),
                p += i[o][m], n -= q[o]) : (i.splice(o, 1), q.splice(o, 1), o -= 1);
        return p
    };

    function qa(a, arr) {
        for (var b, f = c(arr), g = [], h = [], i = [], j = 0, k = f.length; j < k; j++)
            b = e(f[j]), b ? h.push(b) : (g.push(d(f[j][0])),
                h.push(d(f[j][1]))),
                i.push(d(f[j][2]));
        return g.join("") + "!!" + h.join("") + "!!" + i.join("")
    };

    function c(a) {
        for (var b = [], c = 0, d = a.length - 1; c < d; c++) {
            var e = [];
            e[0] = Math.round(a[c + 1][0] - a[c][0]),
                e[1] = Math.round(a[c + 1][1] - a[c][1]),
                e[2] = Math.round(a[c + 1][2] - a[c][2]),
                0 === e[0] && 0 === e[1] && 0 === e[2] || b.push(e)
        }
        return b
    }

    function d(a) {
        var b = "()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr",
            c = b.length,
            d = "",
            e = Math.abs(a),
            f = parseInt(e / c);
        f >= c && (f = c - 1),
            f && (d = b.charAt(f)),
            e %= c;
        var g = "";
        return a < 0 && (g += "!"),
            d && (g += "$"),
            g + d + b.charAt(e)
    }

    function e(a) {
        for (var b = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]], c = "stuvwxyz~", d = 0, e = b.length; d < e; d++)
            if (a[0] == b[d][0] && a[1] == b[d][1])
                return c[d];
        return 0
    }

""")


#  获取滑动轨迹 trace[][] [x, y ,time]
def geeTrace(length):
    trace = []
    trace.append([-random.randint(0, 45), -random.randint(0, 45), 0])
    trace.append([0, 0, 0])
    x = 0
    time = 0
    for index in range(length):
        trace.append([x, 3, time])
        x += 1
        time += random.randint(500, 1000)
    return trace

# 获取userresponse
def getUserresponse(l, challenge):
    return ctx.call("ra", l, challenge)

# 通过Trace获取a参数
def getA(trace):
    return ctx.call("qa", 1490061175124, trace)

# 通过Trace获取passtime
def getPasstime(trace):
    return trace[-1][-1]

# 获取imload参数
def getImload():
    return 43

if __name__ == '__main__':
    print getUserresponse('30', '9f3adf5746ee96ccc729194b95e3d0b05m')
    trace = geeTrace(10)
    print getA(trace)
    print getPasstime(trace)
