SELECT Sname,Sno FROM Student WHERE Scollege_name='信息学院' OR Scollege_name='生工学院';
SELECT AVG(Grade) FROM SC WHERE Cno='EN001';
SELECT Scollege_name AS Scollege_name,COUNT(*) AS Scollege_female_count FROM Student WHERE Ssex='女' GROUP BY Scollege_name;