select b.title title, b.board_id board_id, r.reply_id reply_id, r.writer_id writer_id, r.contents contents, date_format(r.created_date, '%Y-%m-%d') created_date
from used_goods_board b join used_goods_reply r on b.board_id = r.board_id
where b.created_date like '2022-10%'
order by r.created_date asc, b.title asc