FROM gcc:11

ENV TASK_ID "<to_fill>"
ENV CODE "<to_fill>"

COPY cpp/score.sh /userdata/score.sh

COPY examples /userdata/examples

WORKDIR /userdata

ENTRYPOINT bash score.sh
