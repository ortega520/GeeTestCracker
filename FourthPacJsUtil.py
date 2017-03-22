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
        for (var b, c, d, e = [], f = 0, g = [], h = 0, i = a.length - 1; h < i; h++) b = Math.round(a[h + 1][0] - a[h][0]), c = Math.round(a[h + 1][1] - a[h][1]), d = Math.round(a[h + 1][2] - a[h][2]), g.push([b, c, d]), 0 == b && 0 == c && 0 == d || (0 == b && 0 == c ? f += d : (e.push([b, c, d + f]), f = 0));
        return 0 !== f && e.push([b, c, f]), e
    };

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
    };

    function e(a) {
        for (var b = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]], c = "stuvwxyz~", d = 0, e = b.length; d < e; d++)
            if (a[0] == b[d][0] && a[1] == b[d][1])
                return c[d];
        return 0
    };

""")


#  获取滑动轨迹 trace[][] [x, y ,time]
def geeTrace(length):
    trace = []
    trace.append([-random.randint(0, 30), -random.randint(0, 30), 0])
    trace.append([0, 0, 0])
    x = 1
    time = 18
    y = 1
    while x < length:
        if random.randint(0, 1) == 1:
            y += random.randint(-1, 1)
        trace.append([x, y, time])
        if length - x < 5:
            x = length
        else:
            x += random.randint(length/100, length/30)
        if length / 4 < x < length / 2:
            time += random.randint(15, 25)
        else:
            time += random.randint(25, 50)
    trace.append([length, y, time])
    trace.append([length, y, time + 124])
    trace.append([length, y, time + 234])
    trace.append([length, y, time + 441])
    return trace

# 获取userresponse
def getUserresponse(l, challenge):
    res = ctx.call("ra", l, challenge)
    return str(res)

# 通过Trace获取a参数
def getA(trace):
    return ctx.call("qa", 1490061175124, trace)

# 通过Trace获取passtime
def getPasstime(trace):
    return trace[-1][-1]

# 获取imload参数
def getImload():
    return random.randint(30, 100)

if __name__ == '__main__':
    # print getUserresponse('30', '9f3adf5746ee96ccc729194b95e3d0b05m')
    trace = geeTrace(10)
    print trace
    # print getA(trace)
    # print getPasstime(trace)
