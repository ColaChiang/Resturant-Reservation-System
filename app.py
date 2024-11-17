from flask import Flask, jsonify, request, render_template
from reservation_system import ReservationSystem

app = Flask(__name__)
reservation_system = ReservationSystem()

# 初始化訂位資料
existing_reservations = [
    ("0912345678", "王小明"),
    ("0987654321", "李大華"),
    ("0911223344", "張美玲"),
    ("0922334455", "林俊傑"),
    ("0933445566", "陳曉東"),
    ("0966554433", "黃淑芬"),
    ("0955443322", "趙子龍"),
    ("0944332211", "孫悟空"),
    ("0933221100", "周星馳"),
    ("0922110099", "鄭成功"),
    ("0911008877", "胡歌"),
    ("0988776655", "梁朝偉"),
]

# 新增初始訂位
for phone, name in existing_reservations:
    reservation_system.add_reservation(phone, name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    data = request.json
    phone = data.get('phone')
    name = data.get('name')
    if phone and name:
        result = reservation_system.add_reservation(phone, name)
        return jsonify({"message": result})
    return jsonify({"message": "請輸入有效的姓名和電話號碼"}), 400

@app.route('/search_reservation', methods=['GET'])
def search_reservation():
    name = request.args.get('name')
    result = reservation_system.linear_search_reservation(name)
    return jsonify({"message": result})

@app.route('/list_reservations', methods=['GET'])
def list_reservations():
    reservations = reservation_system.list_reservations()
    return jsonify(reservations)

@app.route('/search_by_phone', methods=['GET'])
def search_by_phone():
    phone = request.args.get('phone')
    if phone:
        result = reservation_system.binary_search_reservation(phone)
        return jsonify({"message": result})
    return jsonify({"message": "請輸入有效的電話號碼"}), 400

if __name__ == '__main__':
    app.run(debug=True)
