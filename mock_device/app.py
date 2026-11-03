"""Flask service that simulates a smart-device provisioning lifecycle."""

from __future__ import annotations

from flask import Flask, jsonify, request

app = Flask(__name__)

DEVICE_STATE = {
    "status": "discovered",
    "wifi_connected": False,
    "credentials_sent": False,
    "last_error": None,
}


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
    return jsonify({"status": "ok"}), 200


@app.get("/device")
def device() -> tuple[dict[str, object], int]:
    return jsonify(DEVICE_STATE), 200


@app.post("/scan")
def scan() -> tuple[dict[str, object], int]:
    DEVICE_STATE["status"] = "discovered"
    DEVICE_STATE["last_error"] = None
    return jsonify({"status": "discovered", "message": "device detected"}), 200


@app.post("/connect")
def connect() -> tuple[dict[str, object], int]:
    DEVICE_STATE["status"] = "connected"
    return jsonify({"status": "connected", "message": "BLE linked"}), 200


@app.post("/provision")
def provision() -> tuple[dict[str, object], int]:
    payload = request.get_json(silent=True) or {}
    password = payload.get("password")
    if password == "wrongpass":
        DEVICE_STATE["status"] = "wrong-password"
        DEVICE_STATE["last_error"] = "invalid Wi-Fi credentials"
        return jsonify({"status": "wrong-password"}), 401
    if password == "timeout":
        DEVICE_STATE["status"] = "timeout"
        DEVICE_STATE["last_error"] = "provisioning timed out"
        return jsonify({"status": "timeout"}), 408
    DEVICE_STATE["status"] = "success"
    DEVICE_STATE["wifi_connected"] = True
    DEVICE_STATE["credentials_sent"] = True
    return jsonify({"status": "success", "message": "device provisioned"}), 200


@app.post("/reset")
def reset() -> tuple[dict[str, object], int]:
    DEVICE_STATE.update({
        "status": "discovered",
        "wifi_connected": False,
        "credentials_sent": False,
        "last_error": None,
    })
    return jsonify({"status": "discovered", "message": "device reset"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
