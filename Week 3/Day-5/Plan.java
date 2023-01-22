abstract class Plan {
    protected double rate;
    abstract void getRate();

    public void calculateBill(int units) {
        System.out.println(units*rate);
    }
}

class DomesticPlan extends Plan {
    public void getRate() {
        rate = 3.50;
    }
}

class CommercialPlan extends Plan {
    public void getRate() {
        rate = 7.50;
    }
}

class InstitutionalPlan extends Plan {
    public void getRate() {
        rate = 5.50;
    }
}

class GetPlanFactory {

    public Plan getPlan(String planType) {
        if(planType == null) {
            return null;
        }

        if(planType.equalsIgnoreCase("DOMESTICPLAN")) {
            return new DomesticPlan();
        }

        if(planType.equalsIgnoreCase("InstitutionalPlan")) {
            return new InstitutionalPlan();
        }

        if(planType.equalsIgnoreCase("CommercialPlan")) {
            return new CommercialPlan();
        }

        return null;

    }
    
}