public class Sample {
    private int id;
    public void setId(int value) {
        id = value;
    }
    public int getId() {
        return id;
    }
    private String name;
    public void setName(String value) {
        name = value;
    }
    public String getName() {
        return name;
    }
    private double salary;
    public void setSalary(double value) {
        salary = value;
    }
    public double getSalary() {
        return salary;
    }
    private LocalDate hireDate;
    public LocalDate getHiredate() {
        return hireDate;
    }
    private List<String> skills;
    public void setSkills(List<String> value) {
        skills = value;
    }
    public List<String> getSkills() {
        return skills;
    }

}