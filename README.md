
Requirement
---
- Chemshell
- TURBOMOLE
- DL_POLY
- Python 3.7


Tutorial
---
1.将进行小基组单点计算时所有需要读取的文件放在同一个文件夹内。

2.选取合适的需要进行电荷删除分析的残基（QM区外5-10埃），包括氨基酸和水分子，并将其组合在同一个PDB文件内。将此PDB文件命名。

3.修改python脚本文件和Shell脚本文件的权限：
		Run_order：chmod 750 delete_charge_analysis.py
		Run_order：chmod 750 read_log_to_sum_data.py
		Run_order：chmod 750 qchemsh_multi_jobs.sh

4.仔细阅读delete_charge_analysis.py文件，根据提交任务时读取的文件名和选取的残基进行相应的修改。

5.运行修改后的delete_charge_analysis.py文件：
		Run_order：python3 delete_charge_analysis.py
		
6.运行批处理提交多个计算任务的脚本文件qchemsh_multi_jobs.sh：
		Run_order：bash qchemsh_multi_jobs.sh
		
7.所有计算任务完成后，运行read_log_to_sum_data.py，对每一个定点删除的残基计算输出结果进行批量统计，并得到最终数据统计在sum_data_file.csv文件中。
		Run_order：python3 read_log_to_sum_data.py


Examples
---
Please see the file folder named Example


