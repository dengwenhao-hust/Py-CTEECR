
Requirement
---
- Chemshell
- TURBOMOLE
- DL_POLY
- Python 3.7


Tutorial
---
1.������С���鵥�����ʱ������Ҫ��ȡ���ļ�����ͬһ���ļ����ڡ�

2.ѡȡ���ʵ���Ҫ���е��ɾ�������Ĳл���QM����5-10�����������������ˮ���ӣ������������ͬһ��PDB�ļ��ڡ�����PDB�ļ�������

3.�޸�python�ű��ļ���Shell�ű��ļ���Ȩ�ޣ�
		Run_order��chmod 750 delete_charge_analysis.py
		Run_order��chmod 750 read_log_to_sum_data.py
		Run_order��chmod 750 qchemsh_multi_jobs.sh

4.��ϸ�Ķ�delete_charge_analysis.py�ļ��������ύ����ʱ��ȡ���ļ�����ѡȡ�Ĳл�������Ӧ���޸ġ�

5.�����޸ĺ��delete_charge_analysis.py�ļ���
		Run_order��python3 delete_charge_analysis.py
		
6.�����������ύ�����������Ľű��ļ�qchemsh_multi_jobs.sh��
		Run_order��bash qchemsh_multi_jobs.sh
		
7.���м���������ɺ�����read_log_to_sum_data.py����ÿһ������ɾ���Ĳл�������������������ͳ�ƣ����õ���������ͳ����sum_data_file.csv�ļ��С�
		Run_order��python3 read_log_to_sum_data.py


Examples
---
Please see the file folder named Example


