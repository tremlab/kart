import React from 'react';
import KartItem from './KartItem.jsx';


const Kart = (props) => {
	const items = props.kart;

	if (items.length === 0) {
		return (
			<span>add some items above!</span>
		);
	} else {
		const kartItems = items.map((itm, i) =>
			<KartItem kartItem={itm} key={`${itm.item}-${i}`}/>
		)
		return(
			<div className="KartList">
				<table>
					<tr>
						<th>ITEMS</th>
						<th>QUANTITY</th>
					</tr>
					{ kartItems }
				</table>
			</div>
		)
	}
}

export default Kart;
