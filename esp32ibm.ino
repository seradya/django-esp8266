#include "DHT.h"
#include <WiFi.h>
#include <WiFiClient.h>
#include <PubSubClient.h>

//-------- Configurações de Wi-fi -----------
char* ssid = "Beeline_2G_F43654";           // Nome
char* password = "W123456w";      // Senha

//-------- Conexão IBM - ESP32 -----------
#define ORG "0k740p" // ID de organização
#define DEVICE_TYPE "Esp8266" // Insira o nome do componente
#define DEVICE_ID "seradya" // Insira o ID
#define TOKEN "NDdVf07KBd2vjL(e6d"// Insira o Token

//-------- Comunicação IOT --------
#define DHTPIN 4 // pino que estamos conectado
#define DHTTYPE DHT11 // DHT 11
DHT dht(DHTPIN, DHTTYPE);
char server[] = ORG ".messaging.internetofthings.ibmcloud.com";
char authMethod[] = "use-token-auth";
char token[] = TOKEN;
char clientId[] = "d:" ORG ":" DEVICE_TYPE ":" DEVICE_ID;
const char eventTopic[] = "iot-2/evt/status/fmt/json";
const char cmdTopic[] = "iot-2/cmd/command/fmt/json";

void callback(char* topic, byte* payload, unsigned int payloadLength);
WiFiClient wifiClient;
PubSubClient client(server, 1883, callback, wifiClient);



void setup()
{
  Serial.begin(9600);
  dht.begin();
  pinMode(13, OUTPUT);              // LED13 que será acionado pelo IBM
  pinMode(2, OUTPUT);               // LED2 indica falha na conexão com a internet
  client.setCallback(callback);      // Ajusta a função de retorno
  client.subscribe(cmdTopic);
  wifiConnect();                     // Cria o void wifiConnect
  mqttConnect();
}

//connect wifi
void wifiConnect()
{ // Função void wifiConnect
  Serial.print("Conectando a Rede ");
  Serial.print(ssid);                // Indica a Rede que o ESP32 irá se conectar
  WiFi.begin(ssid, password);        // Conecta ao ssid e o password configurado
  while (WiFi.status() != WL_CONNECTED)
  { // Enquanto estiver desconectado
    delay(500);                      // Aguarda 500 milissegundos
    Serial.print(".");
  }
  Serial.print("Wi-Fi conectado, Endereço de IP: ");
  Serial.println(WiFi.localIP());     // Indica o endereço de IP
}

//connect mqtt
void mqttConnect()
{ // Função void mqttConnect
  if (!!!client.connected())
  {
    Serial.print("Reconectando MQTT do cliente ");
    Serial.println(server);                       // Indica o endereço do servidor
    while (!!!client.connect(clientId, authMethod, token) )
    {
      Serial.print(".");
      delay(500);
    }
    if (client.subscribe(cmdTopic))
    {
      Serial.println("Resposta OK");              // Se a resposta for OK
      digitalWrite(2, LOW);                            // LED 2 OFF
    }
    else
    {
      Serial.println("Resposta FALHOU");   // Se a resposta falhar
      digitalWrite(2, HIGH);                          // LED 2 ON
    }
  }
}
 
void loop() 
{
  if (!client.loop())
  {
    mqttConnect();
  }
  // testa se retorno é valido, caso contrário algo está errado.
  if (isnan((float)dht.readHumidity()) || isnan((float)dht.readTemperature())) 
  {
    Serial.println("Failed to read from DHT");
    delay(2000); 
  } 
  else
  {    
    String payload = "{\"humidity\":{\"value\":";      // Inicia uma String associando ao endereço
    payload += (dht.readHumidity());                 // Atribui o valor de leitura de temperatura a String
    payload += "},";
    payload += "\"temperature\":{\"value\":";
    payload += (dht.readTemperature());
    payload += "}}";                          // Finaliza a String
   
    Serial.print("Enviando payload: ");
    Serial.println(payload);                  // Escreve a String no monitor Serial
    client.publish(eventTopic, (char*) payload.c_str() );  // Publica a String
    delay(500); 
    }  
}

void callback(char* topic, byte* payload, unsigned int payloadLength)
{
  //armazena msg recebida em uma sring
  payload[payloadLength] = '\0';
  String MSG = String((char*)payload);
  
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  Serial.print(MSG);
  if ((char)payload[0] == '0')
  { // Caso receba o caractere 0
    digitalWrite(22, LOW);        // Desliga o LED
    Serial.println("LOW");
  }
  if ((char)payload[0] == '1')
  { // Caso receba o caractere 1
    digitalWrite(22, HIGH);        // Liga o LED
    Serial.println("HIGH");
  }
}