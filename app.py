from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
command = {"cmd": "none", "arg": ""}

@app.route("/")
def control():
    return render_template_string("""
    <h2>Remote xArm Control</h2>
    <button onclick="send('run_pytest')">Run Pytest Suite</button>
    <button onclick="send('run_gripper', 'credit_tap')">Tap Credit</button>
    <button onclick="send('run_gripper', 'debit_insert')">Insert Debit</button>
    <script>
      function send(cmd, arg="") {
        fetch("/command", {
          method: "POST",
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({cmd: cmd, arg: arg})
        });
      }
    </script>
    """)

@app.route("/command", methods=["GET", "POST"])
def get_set_command():
    global command
    if request.method == "POST":
        command = request.json
        return jsonify({"status": "ok"})
    return jsonify(command)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
