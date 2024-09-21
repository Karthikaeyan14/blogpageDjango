from typing import Any
from app.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="This commands inserts post data"
    
    def handle(self, *args: Any, **options: Any):
        #delete existing data

        Post.objects.all().delete
        titles=[

    "The Future of AI",
    "Climate Change Solution",
    "Remote Work Trends",
    "Quantum Computing Explanied",
    "Renewable Energu Innovations",
    "Deep Learning Demystified"
    "Post-Pandemic Econmic Outlook"
     "The Future of AI",
    "Climate Change Solution",
    "Remote Work Trends",
    "Quantum Computing Explanied",
    "Renewable Energu Innovations",
    "Deep Learning Demystified"
    "Post-Pandemic Econmic Outlook"
     "The Future of AI",
    "Climate Change Solution",
    "Remote Work Trends",
    "Quantum Computing Explanied",
    "Renewable Energu Innovations",
    "Deep Learning Demystified"
]

        contents=[
    "Exploring the future of artificial intelligence and its impact on society.",
    "Discovering solutions to combat climage change and protect the environment.",
    "Analyzing trends and challenges in remote work envionments.",
    "An introudction to the principles and applications of quantum computing.",
    "Exploring the future of artificial intelligence and its impact on society.",
    "Discovering solutions to combat climage change and protect the environment.",
    "Analyzing trends and challenges in remote work envionments.",
    "An introudction to the principles and applications of quantum computing.",
    "Exploring the future of artificial intelligence and its impact on society.",
    "Discovering solutions to combat climage change and protect the environment.",
    "Analyzing trends and challenges in remote work envionments.",
    "An introudction to the principles and applications of quantum computing.",
    "Exploring the future of artificial intelligence and its impact on society.",
    "Discovering solutions to combat climage change and protect the environment.",
    "Analyzing trends and challenges in remote work envionments.",
    "An introudction to the principles and applications of quantum computing.",
    "Exploring the future of artificial intelligence and its impact on society.",
    "Discovering solutions to combat climage change and protect the environment.",
    "Analyzing trends and challenges in remote work envionments.",
    "An introudction to the principles and applications of quantum computing.",
]

        img_urls=[
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400",
  
 ]


        for title,content,img_url in zip(titles,contents,img_urls):
            Post.objects.create(title=title,content=content,img_url=img_url)

        
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))



