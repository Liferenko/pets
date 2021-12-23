install_all_i_need:
	# UPD it did not work 
	pkg install python groff
	pip3 install awscli

start_aws_instance:
	aws ec2 start-instances --instance-ids %ID%

stop_aws_instance:
	aws ec2 stop-instance --instance-ids %ID%

ssh_to_aws_instance:
	start_aws_instance
	ssh %username%@%address%
