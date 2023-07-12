#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

const char* ssid = "Your WiFi SSID";       // Имя вашей Wi-Fi сети
const char* password = "Your WiFi Password";   // Пароль вашей Wi-Fi сети
const char* server = "Your Server IP Address";  // IP-адрес вашего веб-сервера Django

const sensorPin = 13;

void setup() {
  Serial.begin(115200);   // Инициализация последовательного порта для вывода отладочной информации

  WiFi.begin(ssid, password);   // Подключение к Wi-Fi сети

  while (WiFi.status() != WL_CONNECTED) {   // Ожидание установления соединения с Wi-Fi
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  WiFiClient client;  

  Serial.println("Connected to WiFi");
}

void loop(){
	int motionValue = digitalRead(sensor1Pin);
	
	if (motionValue == 1){
		motionValue = 4;
		post_data();
	}
	delay(1000);
}

void post_data() {
  // Формирование строки URL с данными
  String url = "http://" + String(server) + "/data/";

  // Создание объекта HTTPClient
  HTTPClient http;

  // Установка URL и типа контента запроса
  http.begin(client, url);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  // Формирование тела запроса с данными датчиков
  String requestBody = "sensor1=" + String(motionValue);

  // Отправка POST запроса с данными датчиков
  int httpResponseCode = http.POST(requestBody);

  if (httpResponseCode > 0) {
    String response = http.getString();   // Получение ответа от сервера
    Serial.println(httpResponseCode);
    Serial.println(response);
  } else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }

  http.end();   // Завершение HTTP-соединения

}
