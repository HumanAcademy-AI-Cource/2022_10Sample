const ros = new ROSLIB.Ros({ url: "ws://" + location.hostname + ":9000" });
ros.on("connection", () => { console.log("websocket: connected"); });
ros.on("error", (error) => { console.log("websocket error: ", error); });
ros.on("close", () => { console.log("websocket: closed"); });


const servo = new ROSLIB.Topic({
    ros: ros,
    name: "/servo",
    messageType: "std_msgs/UInt8",
});

let servo_position = 50
servo.publish(new ROSLIB.Message({
    data: servo_position
}));


document.getElementById("left-button").onclick = () => {
    console.log("left-button")
    servo_position += 1
    if(servo_position > 90){
        servo_position = 90;
    }
    const message = new ROSLIB.Message({
        data: servo_position
    });
    servo.publish(message);
}

document.getElementById("right-button").onclick = () => {
    servo_position -= 1
    if(servo_position < 30){
        servo_position = 30;
    }
    const message = new ROSLIB.Message({
        data: servo_position
    });
    servo.publish(message);
}


setInterval(() => {
    const dateTime = new Date(Date.now());
    let dateString = `${dateTime.getFullYear()}年${dateTime.getMonth() + 1}月${dateTime.getDate()}日 ${dateTime.getHours()}時${dateTime.getMinutes()}分${dateTime.getSeconds()}秒`
    document.getElementById("date").innerHTML = "【現在時刻】" + dateString
}, 1000)

const image_raw = new ROSLIB.Topic({
    ros: ros,
    name: "/usb_cam/image_raw/compressed",
    messageType: "sensor_msgs/CompressedImage",
});

const raspi_temp = new ROSLIB.Topic({
    ros: ros,
    name: "/raspi_temp",
    messageType: "sensor_msgs/Temperature",
});

const raspi_memory = new ROSLIB.Topic({
    ros: ros,
    name: "/raspi_memory",
    messageType: "std_msgs/Float64",
});

image_raw.subscribe((message) => {
    const base64image = "data:image/jpeg;base64," + message.data;
    document.getElementById("image").src = base64image;
});

raspi_temp.subscribe((message) => {
    document.getElementById("temp").innerHTML = message.temperature.toFixed(1) + "℃"
});

raspi_memory.subscribe((message) => {
    document.getElementById("memory").innerHTML = message.data.toFixed(1) + "%"
});