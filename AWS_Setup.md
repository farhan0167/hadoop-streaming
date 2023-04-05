# Setting Up AWS EC2 Instance


In order to run Hadoop, I stayed away from running this on my localhost. I chose to run Hadoop on an AWS EC2 instance, and here's how you can set it up yourself in case you don't know how to.

1. Log in to your [AWS console](https://aws.amazon.com)
2. In your console, use the search bar to search for "EC2". Click on EC2 under Services.
3. Navigate to Launce Instance and click Launce Instance->Launce Instance.
4. Set a name for your server, i.e, hadoop-demo
5. For the Application and OS Images (Amazon Machine Image), select the Ubuntu image. Make sure you're using the x86 architecture.
6. For Instance type, select t3.medium or t3.large. It will charge you by the hour, but you can delete your instance to prevent incuring any charges.
7. For Key pair (login), select Create new key pair. Enter your key name, select RSA and .pem, and Create pair. Save this in your localhost and remember where you are saving it (you'll need it to ssh into the instance)
8. You can leave the remainder of the configs as default, and hit Launch Instance.

This will spin up a new EC2 instance for you, and then you can go to that instance and SSH into it.

## To SSH into instance:
1. Once you are in the EC2 instance you created, click Connect.
2. On the nav pane of the popup, select SSH client.
3. Follow the instructions. Open up your terminal where you saved your key.
4. Run this command
```bash
chmod 400 key_name.pem
```
This is important so that your key is publicly viewable
5. Then connect to your EC2 instance
```bash
ssh -i "key_name.pem" ubuntu@ec2-public-ip.compute-1.amazonaws.com
```
Make sure to follow the instructions in the popup. Simply copy pasting those info will enable you to SSH into your EC2 instance.

6. If everything went okay, you'll be able to now access your EC2 instance from your terminal