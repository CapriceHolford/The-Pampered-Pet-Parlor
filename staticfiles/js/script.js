// FAQ data with categories and questions
const faqData = [
    {
        category: "Booking and Appointments",
        questions: [
            {
                question: "How do I book an appointment?",
                answer: "Did you know you can now book online? It's much easier and quicker! Simply navigate to the menu at the top and select 'Book Online.' Alternatively, you can still book an appointment or make inquiries by calling our salon. Please note that bookings cannot be made via email, but you are welcome to make inquiries. We look forward to assisting you!"
            },
            {
                question: "I'm new to pet grooming, what should I expect?",
                answer: "First of all, a big thank you for coming to visit. Every pet that comes in to be groomed is treated like our own pet, so they're in good hands with us. On your first visit, we'll get you and your pet registered on our system and ask a few questions to better understand what type of groom you'd like. We'll also use our expertise to help guide you on any breed-specific considerations. This will be documented on our 'grooming contract.' We can also give you a tour of our salon and take you behind the scenes to reassure you that your pet's care is our top priority."
            },
            {
                question: "Why do you charge a deposit for my pet's groom?",
                answer: "Our deposits act as a guarantee of your slot. If you cancel or change within 48 hours of the appointment, we can refund your deposit or carry it over to your next appointment. We currently ask for a 20% deposit per pet."
            },
            {
                question: "What size is my dog?",
                answer: "S- Small dogs less than 22 pounds (0-8kg), M- Medium dogs 24 to 33 pounds (9kg-15kg), L- Large dogs 33 to 66 pounds (15kg-30kg), XL- Extra Large dogs 66 or more pounds (30kg and over)"
            }
        ]
    },
    {
        category: "Our Services",
        questions: [
            {
                question: "What if my pet just needs a bath or a trim?",
                answer: "We offer a wide range of services for all pets. If your pet doesn't need a full groom, we offer services such as a Bath, Brush & Blow Dry or a Face Tidy to keep on top of essential grooming needs."
            },
            {
                question: "How long will the groom take?",
                answer: "This depends on breed, size, coat type, and style requirements. Our expert groomers will give you a collection time when you drop your pet off."
            },
            {
                question: "When should my puppy/kitten have their first groom?",
                answer: "We recommend starting grooming with a bath and tidy at least ten days after the final vaccinations. Bring an item with a familiar scent for your pet to help maintain scent continuity."
            }
        ]
    },
    {
        category: "Your Pet's Care",
        questions: [
            {
                question: "Can you remove knots and matts from my pet's coat?",
                answer: "We can remove mats using various methods, but this depends on factors like the severity of the mats and the pet's temperament. Regular grooming and brushing at home will prevent mats."
            },
            {
                question: "Can I stay with my pet whilst they're being groomed?",
                answer: "For safety reasons, owners are not permitted to stay during the groom, but you can stay nearby if you wish."
            },
            {
                question: "Do you use drying cabinets?",
                answer: "We usually use free-standing dryers. In some cases, we may use a drying cabinet. Pets with specific conditions or short-nosed dogs will never be put into drying cabinets."
            },
            {
                question: "If my pet is pregnant or in season, can they still be groomed?",
                answer: "Unfortunately, we cannot groom pets that are pregnant or in season."
            },
            {
                question: "What if my pet is aggressive, can they still be groomed?",
                answer: "If your pet is aggressive, we need to know so we can take necessary precautions. Some aggressive pets may need to come in at the end of the day, and an additional charge will apply."
            }
        ]
    },
    {
        category: "General",
        questions: [
            {
                question: "Free 24 hour correction service",
                answer: "We offer a free correction service for the first 24 hours after collection if you're not satisfied with the groom."
            },
            {
                question: "Is there anything I need to do before my pet comes in?",
                answer: "Please do not feed your pet within 30 minutes of their appointment and ensure they have the opportunity to go to the toilet before entering the salon."
            },
            {
                question: "What if I'm running late to drop my pet off or pick them up?",
                answer: "If you're running late, let us know as soon as possible. If you're more than 15 minutes late, we can't guarantee your appointment. If you don't collect your pet at the agreed collection time, there'll be an additional charge of £5 for every 30 minutes we hold your pet after this time."
            },
            {
                question: "What if I need to make a complaint about the groom?",
                answer: "If you're unhappy with your groom, please contact us via phone or email. We'll respond within 72 hours."
            }
        ]
    }
];

// Function to dynamically generate FAQ content
function generateFAQs() {
    const faqAccordion = document.getElementById('faqAccordion');

    faqData.forEach((category, index) => {
        let accordionSection = `
            <div class="accordion" id="accordion${index}">
                <h3>${category.category}</h3>
                ${category.questions.map((q, i) => `
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="heading${index}-${i}">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${index}-${i}" aria-expanded="false" aria-controls="collapse${index}-${i}">
                                ${q.question}
                            </button>
                        </h2>
                        <div id="collapse${index}-${i}" class="accordion-collapse collapse" aria-labelledby="heading${index}-${i}" data-bs-parent="#accordion${index}">
                            <div class="accordion-body">
                                ${q.answer}
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
        faqAccordion.innerHTML += accordionSection;
    });
}

// Expand/Collapse All Function
document.getElementById('toggleAll').addEventListener('click', () => {
    const allAccordions = document.querySelectorAll('.accordion-collapse');
    const isExpanded = allAccordions[0].classList.contains('show'); // Check if the first accordion item is expanded

    if (isExpanded) {
        // Collapse all
        allAccordions.forEach(accordion => accordion.classList.remove('show'));
        document.getElementById('toggleAll').textContent = 'Expand All'; // Change button text
    } else {
        // Expand all
        allAccordions.forEach(accordion => accordion.classList.add('show'));
        document.getElementById('toggleAll').textContent = 'Collapse All'; // Change button text
    }
});

// Search Function to filter questions
document.getElementById('faqSearch').addEventListener('input', function () {
    const query = this.value.toLowerCase();
    const faqItems = document.querySelectorAll('.accordion-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.accordion-button').textContent.toLowerCase();
        if (question.includes(query)) {
            item.classList.remove('hidden'); // Show the item
        } else {
            item.classList.add('hidden'); // Hide the item
        }
    });
});

// Call the function to generate FAQs on page load
document.addEventListener('DOMContentLoaded', generateFAQs);
