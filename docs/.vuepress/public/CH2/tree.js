
var drawTree = function (ctx, startX, startY, length, depth, angle, branchWidth, angleFixed, color, ifDrawFlower) {
    var defaultAngle = Math.PI / 2, defaultPercent = 0.1, direction = angle < 0 ? -1 : 1,
        defaultTime = 50, rand = Math.random, defaultBranchesNumber = angleFixed ? 2 : 3 * Math.random() + 1,
        newAngle, newLength, timing = angleFixed ? 10 : 20;
    var endX = startX + length * Math.cos(angle),
        endY = startY + length * Math.sin(angle);
    if(--depth <= 0)
        return true;
    ctx.lineCap = "round";
    ctx.lineWidth = branchWidth;
    ctx.strokeStyle = color == null ? "rgb(0, " + (((rand() * 64) +128) >>0) + ",0)" : color;
    var func = function(mStartX, mStartY, mEndX, mEndY){
        ctx.beginPath();
        ctx.moveTo(mStartX, mStartY);
        ctx.lineTo(mEndX, mEndY);
        ctx.stroke();
        ctx.closePath();
    };  func(startX, startY, endX, endY);

    branchWidth *= 0.55;
    for(var i = 0; i < defaultBranchesNumber; i++){
        newAngle = angleFixed ? i == 0 ? angle + defaultAngle / 3 : angle + defaultAngle / -3 : angle + defaultAngle * rand() - defaultAngle / 2;
        newLength = angleFixed ? length * 0.7 : length * (rand() * 0.55 + 0.4);
        if(depth == mDepth - 1 && !angleFixed)
            newAngle = defaultAngle * direction * (rand() * 0.3 + 0.8);
        setTimeout(function (funcAngle, funcLength) {
            drawTree(ctx, endX, endY, funcLength, depth, funcAngle, branchWidth, angleFixed, color, ifDrawFlower);
        }, timing, newAngle, newLength)
    }
};

var canvas = document.getElementById("canvas_tree");
var context = canvas.getContext("2d");
var mDepth = 12;
setTimeout(function () {
    drawTree(context, 750, 700, 170, mDepth, Math.PI / -2, 9, false, null, true);
}, 0);