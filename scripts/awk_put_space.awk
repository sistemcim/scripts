BEGIN{
	FS=""
	str=""
}

{
	for(i=1;i<NF;i++){
		if(i%8==0){
			str1=str1 $i;
			str=str str1 " ";
			str1="";
		}else{
			str1= str1 $i;
		}
	}
} 

END{
	print str;
}

