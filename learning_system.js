class SmartLearningSystem {

    constructor() {
        this.weeklyFocus ='MERN + Security',
        this.dailyTime = 4; //hours
        this.currentLevel = 'Intermediate Beginner';
        this.targetLevel = 'Job Ready FreeLancer';
    }

        setWeeklyFocus(priority) {
        const priorities = {
            'مهم وعاجل': ['إصلاح أخطاء الإنتاج', 'نظام معالجة الأخطاء', 'understand the tools and new knowledge by deep', 'enhance of the logical think'],
            'مهم وغير عاجل': ['تعلم Docker', 'تحسين الـSecurity', 'worked on PFE Collaborate Project'],
            'غير مهم وعاجل': ['إصلاح bugs بسيطة', 'تحسين الـUI'],
            'غير مهم وغير عاجل': ['تعلم تقنيات جديدة', 'مشاريع جانبية', 'posts in my linkedin and my pages to share the learning process', ]
        };
        
        console.log(`🎯 الأولوية لهذا الأسبوع: ${priority}`);
        console.log('المهام:', priorities[priority]);
    }
    
    // طريقة التعلم المناسبة لك
    getLearningMethod(topic) {
        const methods = {
            'تقنية جديدة': '30% نظرية → 70% تطبيق',
            'مشكلة تقنية': 'حاول 30 دقيقة → ابحث → استخدم AI للشرح فقط',
            'مشروع عملي': 'خطط → نفذ → اختبر → راجع',
            'تحضير للفريلانس': 'بناء Portfolio → عروض أسعار → التواصل'
        };
        
        return methods[topic] || 'التعلم العميق بالممارسة';
    }
}

// استخدام النظام
const mySystem = new SmartLearningSystem();
mySystem.setWeeklyFocus('مهم وعاجل');
console.log(mySystem.getLearningMethod('مشكلة تقنية'));


