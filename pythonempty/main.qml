import QtQuick

Window {
    width: 480
    height: 320
    visible: true

    // Item {
    //     id: glassPane
    //     z: 10000
    //     anchors.fill: parent

    //     PointHandler {
    //         id: handler
    //         acceptedDevices: PointerDevice.Mouse | PointerDevice.TouchScreen
    //                          | PointerDevice.TouchPad
    //         target: Rectangle {
    //             parent: glassPane
    //             color: "red"
    //             visible: handler.active
    //             x: handler.point.position.x - width / 2
    //             y: handler.point.position.y - height / 2
    //             width: 20
    //             height: width
    //             radius: width / 2
    //         }
    //     }
    //     Rectangle {
    //         width: 100
    //         height: 100
    //         color: "lightsteelblue"
    //         DragHandler {}
    //     }
    // }
    Item {
        width: 200
        height: 200

        Rectangle {
            anchors.centerIn: parent
            width: text.implicitWidth + 20
            height: text.implicitHeight + 10
            color: "green"
            radius: 5

            Drag.dragType: Drag.Automatic
            Drag.supportedActions: Qt.CopyAction
            Drag.mimeData: {
                "text/plain": "Copied text"
            }

            Text {
                id: text
                anchors.centerIn: parent
                text: "Drag me"
            }

            DragHandler {
                id: dragHandler
                onActiveChanged: if (active) {
                                     parent.grabToImage(function (result) {
                                         parent.Drag.imageSource = result.url
                                         parent.Drag.active = true
                                     })
                                 } else {
                                     parent.Drag.active = false
                                 }
            }
        }
    }
}
