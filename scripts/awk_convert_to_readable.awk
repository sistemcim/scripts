BEGIN{
	FS=" "
	result=""
} 

{
	for(i=1;i<NF;i++){
		total=0
		chr=""
#		print "Order:" i " Binary Number:" $i;
		split($i,arr,"")
		for(j=8;j>0;j--){
			subtotal = arr[j]*(2^(8-j));
#			print "Binary:"arr[j] " Exponent:" 2^(8-j) " Result:" subtotal;
			total += subtotal;
		}
		chr=sprintf("%c",total)
#		print "Total:" total " Character:" chr "\n";
		result= result chr;
	}	
}

END{
	print "\n\n" result;
}

