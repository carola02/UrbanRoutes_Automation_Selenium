Abrir la pagina
Buscar pagina Urban Routes
# Tiempo de espera
1 localizador "Campo Desde" by ID "from"
send keys 'East 2nd Street, 601'
2 localizador "Campo Hasta" by ID "to"
send keys '1300 1st St
Wait implicita hasta que cargue el elemento "by classs "button round"
driver...by class "button round".click
3 localizador BY.ID="tariff-card-4".click
4 localizador By.class "Número de teléfono".CLICK
Wait imlicita hasta que cargue la ventana "by.class "button full" "siguiente"
5 localizador "phone" by.ID "phone"
send keys '+1 123 123 12 12'
"by.class "button full".click
wait imlicita hasta que cargue la ventana By.LINK_TEXT, "Introduce el código del SMS")
6 localizador by ID "code"
llamar la funcion y me reciba el code
sendkeys"code"
6 localizador by class " button full" "Confirmar"
7 localizador by class="pp-text" "Método de pago".click
wait implicito que cargue la ventana by.class "section active"
8 localizador by.class="pp-plus-container".click
wait implicito que cargue el texto by.link text "Agregar tarjeta"
9 localizador by.ID "number"
send.keys "1234 5678 9100" y hacer un tab
10 localizador by.ID "code"
send.keys "111" y hacer un tab
11 localizador by.link test "Agregar".click
12 localizador by.class "close-button section-close".click
13 localizador by. ID"comment"
send.keys "Muéstrame el camino"
14 localizador by lint text " Requisitos del pedido".click
# pendeinte deslizador mantas y pañuelos
<div class="r-sw-container"><div class="r-sw-label">Manta y pañuelos</div><div class="r-sw"><div class="switch"><input type="checkbox" class="switch-input"><span class="slider round"></span></div></div></div>
click slider round
15 localizador, by link text "helado"
# <div class="r-counter-container"><div class="r-counter-label">Helado</div><div class="r-counter"><div class="counter"><div class="counter-minus disabled">–</div><div class="counter-value">0</div><div class="counter-plus">+</div></div></div></div>
hacer 1 click
despues hacer 1 click
16 localizador by class " Pedir un taxi"
<button type="button" class="smart-button"><span class="smart-button-main">Pedir un taxi</span><span class="smart-button-secondary">El recorrido será de 1 kilómetros y se hará en 1 minutos</span></button>
click
Wait explicito 35 segundos
17 localizador by class "order-button".click
assert lugar de recogida == East 2nd Street, 601
assert lugar de destiono == 1300 1st St
DRIVER.QUIT()