import rabbitpy

url = 'amqp://guest:guest@localhost:5672/%2F'
connection = rabbitpy.Connection(url)
channel = connection.channel()

exchange = rabbitpy.Exchange(channel, 'chapter2-example')
exchange.declare()
queue = rabbitpy.Queue(channel, 'example')
queue.declare()
queue.bind(exchange, 'example-routing-key')

for i in range(0, 10):
    message = rabbitpy.Message(channel,'Test message #%i' % i, {'content_type':'text/plain'}, opinionated=True)
    message.publish(exchange, 'example-routing-key')
