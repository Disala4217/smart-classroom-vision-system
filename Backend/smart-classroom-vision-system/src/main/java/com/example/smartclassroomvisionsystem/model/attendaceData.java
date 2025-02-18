package com.example.smartclassroomvisionsystem.model;
import com.example.smartclassroomvisionsystem.services.attendanceDataService;
import java.util.List;
public class attendaceData {
    String Grade;
    public List<String> getEngagement() {
        return Engagement;
    }
    public void setEngagement(List<String> engagement) {
        Engagement = engagement;
    }
    List<String> Engagement;
    attendanceDataService ADS = new attendanceDataService();
    int totalStudents;
    int TotalClases;
    int TotalAttendance;
    int avgAttendence;
    public List<String> getStudentNames() {
        return studentNames;
    }
    public void setStudentNames(List<String> studentNames) {
        this.studentNames = studentNames;
    }
    public List<String> getStudentIDs() {
        return studentIDs;
    }
    public void setStudentIDs(List<String> studentIDs) {
        this.studentIDs = studentIDs;
    }
    public List<String> getClasses() {
        return classes;
    }
public void setClasses(List<String> classes) {
        this.classes = classes;
    }
    public List<String> getClassAttendance() {
        return classAttendance;
    }
    public void setClassAttendance(List<String> classAttendance) {
        this.classAttendance = classAttendance;
    }
    List<String> studentNames;
    List<String> studentIDs;
    List<String> classes ;
    List<String> classAttendance;
    public int getTotalEngagement() {
        return TotalEngagement;
    }
    public void setTotalEngagement(int totalEngagement) {
        TotalEngagement = totalEngagement;
    }
    int AvgEngagment;
    int TotalEngagement;
    public int getTotalStudents() {
        return totalStudents;
    }
    public void setTotalStudents(int totalStudents) {
        this.totalStudents = totalStudents;
    }
    public void setGrade(String grade) {
        Grade = grade;
    }
    public int getTotalClases() {
        return TotalClases;
    }
    public void setTotalClases(int totalClases) {
        TotalClases = totalClases;
    }
    public int getTotalAttendance() {
        return TotalAttendance;
    }
    public void setTotalAttendance(int totalAttendance) {
        TotalAttendance = totalAttendance;
    }
    public void setAvgAttendence(int avgAttendence) {
        this.avgAttendence = avgAttendence;
    }
    public int attendaceSummeryData() {
        if (totalStudents == 0 || TotalClases == 0) {
            return 0;
        }
        avgAttendence = (int) ((TotalAttendance / (double) (totalStudents * TotalClases)) * 100);
        setAvgAttendence(avgAttendence);
        return avgAttendence;
    }
    public int Engagment() {
        if (totalStudents == 0 || TotalClases == 0) {
            return 0;
        }
        AvgEngagment = (int) ((TotalEngagement / (double) (totalStudents * TotalClases*100)) * 100);
        setAvgAttendence(AvgEngagment);
        return AvgEngagment;
    }
    public void modelVariableFiller() {
        setTotalEngagement((int) Double.parseDouble(ADS.totalEngagment(Grade)));
        System.out.println("Total Engagement: " + getTotalEngagement());
        setTotalAttendance((int) Double.parseDouble(ADS.totalattendence(Grade)));
        System.out.println("Total Attendance: " + getTotalAttendance());
        setTotalStudents(Integer.parseInt(ADS.totalStudent(Grade)));
        System.out.println("Total Students: " + getTotalStudents());
        setTotalClases(Integer.parseInt(ADS.totalclasses(Grade)));
        System.out.println("Total Classes: " + getTotalClases());
    }
    public void AttendenceDetail(String grade) {
        setStudentNames(ADS.GetStudentNames(grade));
        setStudentIDs(ADS.GetStudentID(grade));
        setClasses(ADS.GetClassesForGrade(grade));
       setClassAttendance(ADS.GetStudentsAttendedForClasses(grade));
    }
    public void EngagmentDetail(String grade) {
        setStudentNames(ADS.GetStudentNames(grade));
        setStudentIDs(ADS.GetStudentID(grade));
        setClasses(ADS.GetClassesForGrade(grade));
        setEngagement(ADS.GetStudentsEngagementForClasses(grade));
    }
}
