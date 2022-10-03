<?php

/*
 * file : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.4_change_file_name\s-5\g-5_s-5.php
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.4_change_file_name\s-5\
php g-5_s-5.php
 */

function test_1() {
	
	echo ("yesss.");
	
	/********************
	* vars
	********************/
	$msg	= "yeeeeees";
	
	printf("[%s : %d] %s", basename(__FILE__), __LINE__, $msg);
	
	$dpath_Target	= "G:\\images\\2022";
	
	$listOf_Entries	= array_diff(scandir($dpath_Target), array('.', '..'));
	$listOf_Entries__Dir	= array();
	
// 	print_r($listOf_Entries);

	foreach ($listOf_Entries as $entry) {
	
		//ref https://www.w3schools.com/php/func_filesystem_is_dir.asp
		if (is_dir($dpath_Target . "\\" . $entry)) {
			
			// push
			array_push($listOf_Entries__Dir, $entry);
		
// 			$msg	= "dir : $entry";
			
			//ref https://www.w3schools.com/php/func_string_printf.asp
// 			printf("[%s : %d] %s", 
// 							__FILE__, __LINE__, $msg);
			
// 			print ("\n");
		
		} else {
		
// 			$msg	= "file : $entry";
				
// 			printf("[%s : %d] %s",
// 					__FILE__, __LINE__, $msg);
			
// 			print ("\n");
			
		}//if (is_dir($dpath_Target . "\\" . $entry))
		
		/********************
		* show
		********************/
		foreach ($listOf_Entries__Dir as $dir) {
		
			printf("[%s : %d] dir : %s", 
// 							__FILE__, __LINE__, basename($dir));
							__FILE__, __LINE__, $dir);
			
			print ("\n");
			
		}//foreach ($listOf_Entries__Dir as $dir)
		
		
		
	}//foreach ($listOf_Entries as $entry)
	
	
	
	;
}//function test_1() {

function get_dir_list($dpath_Target) {

// 	echo ("yesss.");

	/********************
	 * vars
	********************/
// 	$msg	= "yeeeeees";

// 	printf("[%s : %d] %s", basename(__FILE__), __LINE__, $msg);

// 	$dpath_Target	= "G:\\images\\2022";

	$listOf_Entries	= array_diff(scandir($dpath_Target), array('.', '..'));
	$listOf_Entries__Dir	= array();

	// 	print_r($listOf_Entries);

	foreach ($listOf_Entries as $entry) {

		//ref https://www.w3schools.com/php/func_filesystem_is_dir.asp
		if (is_dir($dpath_Target . "\\" . $entry)) {
				
			// push
			array_push($listOf_Entries__Dir, $entry);

			// 			$msg	= "dir : $entry";
				
			//ref https://www.w3schools.com/php/func_string_printf.asp
			// 			printf("[%s : %d] %s",
			// 							__FILE__, __LINE__, $msg);
				
			// 			print ("\n");

		} else {

			// 			$msg	= "file : $entry";

			// 			printf("[%s : %d] %s",
			// 					__FILE__, __LINE__, $msg);
				
			// 			print ("\n");
				
		}//if (is_dir($dpath_Target . "\\" . $entry))

		/********************
		 * show
		 ********************/
// 		foreach ($listOf_Entries__Dir as $dir) {

// 			printf("[%s : %d] dir : %s",
// 			// 							__FILE__, __LINE__, basename($dir));
// 					__FILE__, __LINE__, $dir);
				
// 			print ("\n");
				
// 		}//foreach ($listOf_Entries__Dir as $dir)
	
	}//foreach ($listOf_Entries as $entry)

	/********************
	 * return
	 ********************/
	$valOf_Ret	= $listOf_Entries__Dir;
	
	return $valOf_Ret;

	;
}//function get_dir_list() {

function main_func() {
	
	/********************
	* 1. get : dir list	: L1
	********************/
	$dpath_Target	= "G:\\images\\2022";
	
	$listOf_DirName	= get_dir_list($dpath_Target);
	
	/********************
	 * 2. get : dir list : filtered	: L2
	 ********************/
	$listOf_DirName__Filtered	= array();
	
	foreach ($listOf_DirName as $dir_name) {
	
		$keyword	= '/ - .+/';	//=> match
// 		$keyword	= '/ - .+$/';	//=> no match
// 		$keyword	= '/ - /';
		
		//ref https://stackoverflow.com/questions/4366730/how-do-i-check-if-a-string-contains-a-specific-word
		if (preg_match($keyword, $dir_name)) {
		
			printf("[%s : %d] match : %s", __FILE__, __LINE__, $dir_name);
			
			print ("\n");
			
			/********************
			* push to array
			********************/
			array_push($listOf_DirName__Filtered, $dir_name);
			
		}//if (preg_match($keyword, $dir_name))
		;
		
	}//foreach ($listOf_DirName as $dir_name)
	
	/********************
	* report
	********************/
	printf("[%s : %d] list of matches", __FILE__, __LINE__);
	
	print ("\n");
	
	print_r($listOf_DirName__Filtered);
	
	/********************
	 * 3. get : dir list : filtered + erased	: L3
	 ********************/
	$listOf_DirName__Filtered_Erased	= array();
	
	$keyword	= '/ - .+/';
	
	foreach ($listOf_DirName__Filtered as $dir_name) {
	
		$dir_name_Erased	= preg_replace($keyword, "", $dir_name);
		
		printf("[%s : %d] \$dir_name : %s", __FILE__, __LINE__, $dir_name);
		print ("\n");
		
		printf("[%s : %d] \$dir_name_Erased : %s", __FILE__, __LINE__, $dir_name_Erased);
		print ("\n");
		
		// push
		array_push($listOf_DirName__Filtered_Erased, $dir_name_Erased);
		
	}//foreach ($listOf_DirName__Filtered as $dir_name)
	
	/********************
	 * 4. get : list of dpath : new		: L4
	 ********************/
	$listOf_Dpath__New	= array();
	
	foreach ($listOf_DirName__Filtered_Erased as $dir_name) {
	
		$dpath_New = join("\\", array($dpath_Target, $dir_name));
		
		// push
		array_push($listOf_Dpath__New, $dpath_New);
		
	}//foreach ($listOf_DirName__Filtered_Erased as $dir_name)
	
	// report
	printf("[%s : %d] \$listOf_Dpath__New", __FILE__, __LINE__);
	
	print ("\n");
	
	print_r($listOf_Dpath__New);
	
	#mark:20221003_113510
}


main_func();

// get_dir_list();
// test_1();
