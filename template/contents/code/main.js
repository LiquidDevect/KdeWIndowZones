 
function newSlotPosition(workspace, client, numberXslots, numberYslots, x, y, xSlotToFill, ySlotToFill) {
    var maxArea = workspace.clientArea(KWin.MaximizeArea, client);

    var newX = maxArea.x + Math.round(maxArea.width / numberXslots * x);
    var newY = maxArea.y + Math.round(maxArea.height / numberYslots * y);

    var clientWidth = Math.round(maxArea.width / numberXslots * (x + xSlotToFill)) - (newX - maxArea.x);
    var clientHeight = Math.round(maxArea.height / numberYslots * (y + ySlotToFill)) - (newY - maxArea.y);

    return [newX, newY, clientWidth, clientHeight]
}

function reposition(client, newX, newY, w, h) {
    client.frameGeometry = {
        x: newX,
        y: newY,
        width: w,
        height: h
    }
}

function move(workspace, numberXslots, numberYslots, x, y, xSlotToFill, ySlotToFill) {
    var client = workspace.activeClient;
    if (client.moveable && client.resizeable) {
        client.setMaximize(false,false);
        arr = newSlotPosition(workspace, client, numberXslots, numberYslots, x, y, xSlotToFill, ySlotToFill);
        var newX = arr[0],
            newY = arr[1],
            w = arr[2],
            h = arr[3];
        reposition(client, newX, newY, w, h)
    }
}