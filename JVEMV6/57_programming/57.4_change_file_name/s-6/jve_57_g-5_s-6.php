<?php 

	/***
	 * 

file			C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.4_change_file_name\s-6\jve_57_g-5_s-6.php
started at		20221025_105206


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.4_change_file_name\s-6\
echo.>> log_g-5_s-6.log && echo ============================ >> log_g-5_s-6.log && C:\WORKS_2\t.bat >> log_g-5_s-6.log && echo.>> log_g-5_s-6.log && C:\xampp_5.6\php\php.exe jve_57_g-5_s-6.php >> log_g-5_s-6.log
//echo.>> log_g-5_s-6.log && echo ============================ >> log_g-5_s-6.log && C:\WORKS_2\t.bat >> log_g-5_s-6.log && echo.>> log_g-5_s-6.log && jve_57_g-5_s-6.py >> log_g-5_s-6.log


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.4_change_file_name\s-6\
php jve_57_g-5_s-6.php

	 */
	
	/******************** (20 '*'s)
	* function read_lines($fpath)
	* @param	$fpath					: file full path
	* @return	$linesOf_FileContent	: array of lines
	* 
	********************/
	function read_lines($fpath) {
		
		/******************** (20 '*'s)
		* step : 1 : message
		********************/
		printf("[%s : %d] starting : read_lines", basename(__FILE__), __LINE__);
		
		echo "\n";
		
		$linesOf_FileContent	= array();
		
		/******************** (20 '*'s)
		 * step : 2 : read
		 ********************/
		//ref https://www.php.net/manual/en/function.file-get-contents.php
// 		$contentOf_File	= file_get_contents($fpath);
		
// 		printf("[%s : %d] \$contentOf_File :", basename(__FILE__), __LINE__, $contentOf_File);
// 		echo "\n";
		
// 		print_r($contentOf_File);

		
		//ref https://stackoverflow.com/questions/4103287/read-a-plain-text-file-with-php
		$fh = fopen($fpath,'r');
		
		while ($line = fgets($fh)) {
			
			array_push($linesOf_FileContent, $line);
			
		}//while ($line = fgets($fh)) {
		
		fclose($fh);
		
		//message
		printf("[%s : %d] file closed : %s", basename(__FILE__), __LINE__, $fpath);
		echo "\n";
		
		//report
		printf("[%s : %d] file content", basename(__FILE__), __LINE__);
		echo "\n";
		print_r($linesOf_FileContent);

		/******************** (20 '*'s)
		 * step : 3 : return
		 ********************/
		$valOf_Ret	= $linesOf_FileContent;
		
		return $valOf_Ret;
		
	}//function read_lines($fpath) {

	function replace_File_Content(
			$_lines
			, $_aryOf_Strings_Target
			, $_aryOf_Strings_Replace) {
		
		/******************** (20 '*'s)
		* step : 1 : replace
		********************/
		$linesOf_FileContent__Replaced	= array();
		
		foreach ($_lines as $line) {
		
			/******************** (20 '*'s)
			* step : 1 : replace
			********************/
			$line_new	= str_replace(
					$_aryOf_Strings_Target
					, $_aryOf_Strings_Replace
					, $line);
			
			printf("[%s : %d] replacing...", basename(__FILE__), __LINE__);
			
			echo "\n";
			
			printf("[%s : %d] orig : %s / new : %s"
					, basename(__FILE__), __LINE__
					, $line, $line_new);
			
			echo "\n";
			echo "\n";
			
			/******************** (20 '*'s)
			* step : 2 : add to array
			********************/
			array_push($linesOf_FileContent__Replaced, $line_new);
			
		}//foreach ($lines as $line)
	
		/******************** (20 '*'s)
		 * step : 2 : return
		 ********************/
		$valOf_Ret	= $linesOf_FileContent__Replaced;
		
		return $valOf_Ret;
		
	}//	function replace_File_Content($_lines, $_aryOf_Strings_Target, $_aryOf_Strings_Replace) {
	
	function change_File_Names($_lines, $_linesOf_FileContent__Replaced, $_dpath) {
		
		//20221027_113245:next
		
		$lenOf_LinesOf_FileContent	= count($_linesOf_FileContent__Replaced);

		//test
		$dpath		= "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\tmp";
// 		$fname_Orig	= $_lines[0];
// 		$fname_Orig__Trimmed	= trim($fname_Orig);
		
// // 		$fname_Orig	= "2022-12-11~20 - コピー - コピー";
		
// 		$fpath_Orig	= join("\\", array($dpath, $fname_Orig__Trimmed));
// // 		$fpath_Orig	= join("\\", array($dpath, $fname_Orig));
		
		
// // 		$fpath_Orig	= "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\tmp\\2022-12-21~31 - コピー - コピー";
// // 		$fpath_Orig	= "G:\\images\\2022\\2022-12-21~31 - コピー - コピー";
		
// 		//ref https://stackoverflow.com/questions/34078845/convert-from-utf-8-to-shift-jis
// 		$fpath_Orig__Converted	= mb_convert_encoding($fpath_Orig, "SJIS", "UTF-8");
// // 		$fpath_Orig__Converted	= mb_convert_encoding("G:\\images\\2022\\2022-12-21~31 - コピー - コピー", "SJIS", "UTF-8");
		
// 		$fname_New	= $_linesOf_FileContent__Replaced[0];
// 		$fname_New__Trimmed	= trim($fname_New);
		
// // 		$fname_New	= "2022-12-21~31";
		
// 		$fpath_New	= join("\\", array($dpath, $fname_New__Trimmed));
// // 		$fpath_New	= join("\\", array($dpath, $fname_New));
		
// 		//report
// 		printf("[%s : %d] \$fname_Orig : %s", basename(__FILE__), __LINE__, $fname_Orig);
// 		echo "\n";
// 		printf("[%s : %d] \$fpath_Orig : %s", basename(__FILE__), __LINE__, $fpath_Orig);
// 		echo "\n";
// 		printf("[%s : %d] \$fpath_Orig__Converted : %s", basename(__FILE__), __LINE__, $fpath_Orig__Converted);
// 		echo "\n";
// 		printf("[%s : %d] \$fpath_New : %s", basename(__FILE__), __LINE__, $fpath_New);
// 		echo "\n";
		
// // 		$res_Bool	= rename($fpath_Orig, $fpath_New);
// 		$res_Bool	= rename($fpath_Orig__Converted, $fpath_New);
// // 		$res_Bool	= rename($fpath_Orig__Converted, $fname_New);
// 			//=> アクセスが拒否されました。
// // 		$res_Bool	= rename($fpath_Orig, $fname_New);
		
// 		//20221025_122436:next
		
		
		
		for ($i = 0; $i < $lenOf_LinesOf_FileContent; $i++) {
		
			/******************** (20 '*'s)
			 * step : 1 : prep : vars
			 ********************/
			$fpath_Orig	= join("\\", array($_dpath, $_lines[$i]));
			$fname_Orig__Trimmed	= trim($fname_Orig);
			$fpath_Orig	= join("\\", array($dpath, $fname_Orig__Trimmed));
			$fpath_Orig__Converted	= mb_convert_encoding($fpath_Orig, "SJIS", "UTF-8");
			
			
			$fpath_New	= join("\\", array($_dpath, $_linesOf_FileContent__Replaced[$i]));
			
// 			$fname_New	= $_linesOf_FileContent__Replaced[$i];
				
			//report
			printf("[%s : %d] \$fpath_Orig : %s", basename(__FILE__), __LINE__, $fpath_Orig);
			echo "\n";
			printf("[%s : %d] \$fpath_New : %s", basename(__FILE__), __LINE__, $fpath_New);
			echo "\n";
			echo "\n";
				
			/******************** (20 '*'s)
			 * step : 2 : rename
			 ********************/
			//ref https://stackoverflow.com/questions/13434883/rename-file-in-php
// 			$res_Bool	= rename($fpath_Orig, $fname_New);
// 			$res_Bool	= rename($fpath_Orig, $fname_New);
			$res_Bool	= rename($fpath_Orig__Converted, $fpath_New);
			
			printf("[%s : %d] rename result => %d", basename(__FILE__), __LINE__, $res_Bool);
			echo "\n";
			echo "\n";
			
			
			
		}//for ($i = 0; $i < $lenOf_LinesOf_FileContent; $i++)		
		
	}//function change_File_Names($_lines, $_linesOf_FileContent__Replaced, $_dpath) {
	
	
	function main_exec() {
		
		/******************** (20 '*'s)
		 * step : 1 : read file
		 ********************/
		$fname	= "chage_file_names.txt";
// 		$dpath	= "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\tmp";
		$dpath	= "G:\\images\\2022";
		$dpath_Target_Folders	= "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\tmp";
		
		//ref https://stackoverflow.com/questions/1091107/how-to-join-filesystem-path-strings-in-php
		$fpath	= join("\\", array($dpath, $fname));
// 		$fpath	= "G:\\images\\2022\\chage_file_names.txt";
			
		$lines	= read_lines($fpath);
		
		/******************** (20 '*'s)
		 * step : 2 : replace strings
		 ********************/
		$aryOf_Strings_Target	= array("コピー", " - ");
		$aryOf_Strings_Replace	= array("", "");
		
		$linesOf_FileContent__Replaced	= replace_File_Content(
				$lines
				, $aryOf_Strings_Target
				, $aryOf_Strings_Replace);
		
		//debug
		printf("[%s : %d] \$linesOf_FileContent__Replaced ==> ", basename(__FILE__), __LINE__, $linesOf_FileContent__Replaced);
		echo "\n";
		
		print_r($linesOf_FileContent__Replaced);
		
		/******************** (20 '*'s)
		 * step : 3 : change file names
		 ********************/
		change_File_Names($lines, $linesOf_FileContent__Replaced, $dpath_Target_Folders);
// 		change_File_Names($lines, $linesOf_FileContent__Replaced, $dpath);
		

		
		
// 		$linesOf_FileContent__Replaced	= array();
		
// 		foreach ($lines as $line) {
		
// 			/******************** (20 '*'s)
// 			* step : 1 : replace
// 			********************/
// 			$line_new	= str_replace(
// 					$aryOf_Strings_Target
// 					, $aryOf_Strings_Replace
// 					, $line);
			
// 			printf("[%s : %d] replacing...", basename(__FILE__), __LINE__);
			
// 			echo "\n";
			
// 			printf("[%s : %d] orig : %s / new : %s"
// 					, basename(__FILE__), __LINE__
// 					, $line, $line_new);
			
// 			echo "\n";
// 			echo "\n";
			
// 			/******************** (20 '*'s)
// 			* step : 2 : add to array
// 			********************/
// 			array_push($linesOf_FileContent__Replaced, $line_new);
			
// 		}//foreach ($lines as $line)
		
		
		
		
	}//function main_exec() {
	
// 	echo "yes";
	
// 	printf("[%s : %d] yes", __FILE__, __LINE__);
// 	echo "\n";
	
	printf("[%s : %d] yeeeees", basename(__FILE__), __LINE__);
	echo "\n";

	/******************** (20 '*'s)
	* execute
	********************/
	main_exec();
	
?>