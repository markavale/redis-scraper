FROM python:3.8:alpine

ENTRYPOINT ["python"]
CMD ["crawl", "sections"]
