select distinct process_name,exe_path from message where process_name <> '' and process_name <> 'PCWatcher 2.2.exe' and exe_path <> 'F:\PCWatcher\PCWatcher 2.2 Relese\PCWatcher 2.2.exe'
select id,time_stamp,process_name,exe_path from message where process_name = 'liebao.exe' and exe_path = 'F:\PCWatcher\PCWatcher 2.2 Relese\PCWatcher 2.2.exe'
select id,time_stamp,process_name,exe_path from message where exe_path = 'C:\Users\¡·\AppData\Local\Temp\~nsu.tmp\Un_A.exe'
