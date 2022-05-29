from flask import Flask, request, abort
import json
from Pizza import pizzeria

app = Flask(__name__)


@app.route('/pizzeria/menu', methods=['GET'])
def get_menu():
    menu = pizzeria.load_menu()
    pizza_name = request.args.get("pizza_name")
    if pizza_name:
        if pizza_name in menu:
            return json.dumps({pizza_name: menu[pizza_name]})
        else:
            abort(404)
    else:
        return json.dumps(menu)


@app.route('/pizzeria/menu/pizza', methods=['POST'])
def add_pizza():
    data = request.form
    pizza_name = data.get("name")
    pizza_cost = data.get("cost")
    pizzeria.add_pizza(pizza_name, pizza_cost)
    return '', 201


@app.route('/pizzeria/menu/pizza', methods=['DELETE'])
def remove_pizza():
    pizza_name = request.args.get("pizza_name")
    pizzeria.remove_pizza(pizza_name)
    return '', 204


@app.route('/pizzeria/order', methods=['POST'])
def order_pizza():
    data = request.form
    order = data.getlist("order")
    result = pizzeria.order_pizza_api(order)
    if result:
        return json.dumps({'cost': result})
    else:
        abort(404)


if __name__ == "__main__":
    app.run()

# @app.route('/')
# def hello():
#     return "<a href='http://127.0.0.1:5000/weather'>Weather</a>"
#
#
# @app.route('/weather')
# def weather():
#     page = requests.get(
#         "https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D"
#         "0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5")
#     soup = BeautifulSoup(page.text, "html.parser")
#     result = soup.find('div', {'class': 'ArchiveTemp'}).find('span', {'class': 't_0'})
#     return "Текущая погода " + result.text
#
#
# @app.route('/p')
# def page():
#     return render_template('index.html')
