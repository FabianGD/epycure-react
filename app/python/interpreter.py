# interpreter.py
import json

def interpreteMessage(rawMessage):
    """
    Function tries to decode the raw JSON string message and
    returns either a non-null reply or non-null array of work orders
    """
    # Try to load the JSON string. If not successful, return an error message
    try:
        strMessage = rawMessage.decode('ascii')
        message = json.loads(strMessage)
        print(strMessage, message)
    except Exception as e:
        print(e)
        print('Could not decode JSON message')
        return ('DecodeError', False)

    # Try to load the message content.
    # If not successful, return an error message
    try:
        messageContent = message['messageContent']
        print(messageContent.keys())
    except Exception as e:
        print(e)
        return ('DecodeError', False)

    # If both succeeded, do some work from the message data

    if 'randomArray' in messageContent.keys():
        try:
            numberOfElements = int(messageContent['randomArray'])
            return ('order accepted', {'randomArray': numberOfElements})
        except TypeError:
            return ('DecodeError', False)

    if 'string' in messageContent.keys():
        return ('Success with string "{}"'.format(messageContent['string']), False)

    return (False, False)


def misc(message):
    if b'Hello' in message:
        # socket.send_string('World '+str(id))
        pass
    elif b'array' in message:
        basic_json['data'] = generateData()
        socket.send_string(json.dumps(basic_json))
        pass
