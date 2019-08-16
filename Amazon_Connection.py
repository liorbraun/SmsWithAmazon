import boto3

try:
  def AmazonSendSms(phoneNumber, message):
      client = boto3.client('sns', 'eu-west-1')
      client.publish(PhoneNumber=phoneNumber, Message=message)
except:
 print("error in sendsms")